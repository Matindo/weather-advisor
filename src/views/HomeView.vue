<template>
  <div id="home">
    <section class="weather">
      <span class="jumbotron1">
        <h1>Get current weather and forecasts from any location, any time</h1>
      </span>
      <div class="search">
        <input type="text" class="search-bar" placeholder="Search" v-model="searchQuery" @keyup.enter="search()" />
        <button class="search-button" @click="search()">
          <b-icon icon="search"></b-icon>
        </button>
      </div>
      <div class="location">
        <b-button size="sm" variant="outline-light" pill @click="locationWeather()">Get Current Location's Weather</b-button>
      </div>
      <div class="weather-bar">
        <div class="current-weather">
          <weather-widget :weatherDetails="weatherData" />
          <p style="font-size: 1.2rem;">Set this as your default weather location?</p>
          <b-button pill variant="outline-info" @click="setDefaultWeatherLocation">Yes, Set Default Location</b-button>
        </div>
        <div class="forecast">
          <div id="week-forecast">
            <h2>This week's forecast: </h2>
            <div id="casts">
              <b-col v-for="forecast in weatherForecast" :key="forecast.day" class="mx-2 columns">
                <ForecastWidget  :forecast="forecast" />
              </b-col>
            </div>
          </div>
        </div>
        <div class="description">
          <p>*this is a 3-hour weather forecast for five days, starting from the time you refresh or reload this page</p>
        </div>
      </div>
    </section>
    <section class="subscription">
      <span class="jumbotron2">
        <h1>Subscribe to get customized weather messages and alerts</h1>
      </span>
      <div class="regular-user">
        <div class="type">
          <div class="title">Regular User</div>
          <div class="illustrate"><img src="../assets/images/Push notifications-cuate.png" alt="regular" /></div>
          <div class="info">You'll get daily alerts on weather forecasts you want to help you plan your daily activities.</div>
          <b-button class="more p-0" size="sm" variant="outline-primary" @click="regularSubscribe">Subscribe</b-button>
        </div>
      </div>
      <div class="farmer">
        <div class="type">
          <div class="title">Farmer</div>
          <div class="illustrate"><img src="../assets/images/Farmer-rafiki.png" alt="farmer" /></div>
          <div class="info">You'll get weekly and monthly forecasts and predictions to help you plan for your farm activities.</div>
          <b-button class="more p-0" size="sm" variant="outline-success" @click="farmerSubscribe">Subscribe</b-button>
        </div>
      </div>
      <div class="organization">
        <div class="type">
          <div class="title">Relief Organization</div>
          <div class="illustrate">
            <img src="../assets/images/Humanitarian Help-pana.png" alt="ngo" />
          </div>
          <div class="info">You'll get pre-empted weather alerts and warnings to help you prepare for relief activities where needed.</div>
          <b-button class="more p-0" size="sm" variant="outline-danger" @click="orgSubscribe">Subscribe</b-button>
        </div>
      </div>
    </section>
    <b-modal ref="modal-subscribe" size="xl" hide-footer body-bg-variant="dark" body-text-variant="light" header-bg-variant="dark" header-text-variant="light">
      <template #modal-title>
        <h1>Subscribe to Weather Alerts</h1>
      </template>
      <register-form :presets="formOptions" />
    </b-modal>
    <snack-bar />
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue'
import WeatherWidget from '../components/WeatherWidget.vue'
import { locationMixin } from '@/mixins/locationMixin'
import { weatherMixin } from '@/mixins/weatherMixin'
import ForecastWidget from '@/components/ForecastWidget.vue'
import { mapGetters } from 'vuex'
import SnackBar from '@/components/SnackBar.vue'

export default {
  name: 'HomeView',
  components: { RegisterForm, WeatherWidget, ForecastWidget, SnackBar },
  mixins: [locationMixin, weatherMixin],
  data: function () {
    return {
      formOptions: { userType: '' },
      searchQuery: ''
    }
  },
  computed: {
    ...mapGetters({
      city: 'CITY',
      location: 'LOCATION',
      message: 'MESSAGE',
      status: 'STATUS'
    })
  },
  methods: {
    search: function () {
      this.fetchCityWeather(this.searchQuery)
      this.fetchCityForecast(this.searchQuery)
    },
    locationWeather: function () {
      this.getLocation()
      setTimeout(() => {
        if (!this.error) {
          this.fetchCoordinateWeather({ lon: this.longitude, lat: this.lattitude })
          this.fetchCoordinateForecast({ lon: this.longitude, lat: this.lattitude })
          this.searchQuery = ''
        } else {
          this.$bvToast.toast(this.message, {
            title: 'Location Error',
            variant: 'danger',
            autoHideDelay: 5000,
            appendToast: false
          })
        }
      }, 1000)
    },
    setDefaultWeatherLocation: function () {
      if (this.searchQuery !== '') {
        this.$store.dispatch('SET_DEFAULT_CITY', this.searchQuery)
      } else {
        this.$store.dispatch('SET_DEFAULT_LOCATION', [this.longitude, this.lattitude])
      }
    },
    showSubscribeModal: function () {
      this.$refs['modal-subscribe'].show()
    },
    hideSubscribeModal: function () {
      this.$refs['modal-subscribe'].hide()
    },
    regularSubscribe: function () {
      this.formOptions.userType = 'Regular'
      this.showSubscribeModal()
    },
    farmerSubscribe: function () {
      this.showSubscribeModal()
    },
    orgSubscribe: function () {
      this.showSubscribeModal()
    },
    showSnackbar: function () {
      document.getElementById('snackbar').className = 'show'
    }
  },
  mounted: function () {
    if (this.city !== '') {
      this.searchQuery = this.city
      this.fetchCityWeather(this.searchQuery)
      this.fetchCityForecast(this.searchQuery)
    } else if (this.location.length > 0) {
      this.fetchCoordinateWeather({ lon: this.location[0], lat: this.location[1] })
      this.fetchCoordinateForecast({ lon: this.location[0], lat: this.location[1] })
    } else {
      this.searchQuery = 'Nairobi'
      this.fetchCityWeather(this.searchQuery)
      this.fetchCityForecast(this.searchQuery)
    }
    this.$root.$on('footerSubscribe', () => {
      this.showSubscribeModal()
    })
    this.$root.$on('headerSubscribe', () => {
      this.showSubscribeModal()
    })
    this.$root.$on('showSnackbar', () => {
      this.showSnackbar()
    })
  }
}
</script>

<style lang="scss" scoped>
* {
  box-sizing: border-box;
  font-size: 1.5rem;
}

#home {
  display: grid;
  grid-template-rows: min-content max-content;
  grid-template-columns: minmax(auto, 100%);
  grid-template-areas:
    "weather-section"
    "subscription-section";
  align-items: center;
  justify-content: center;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
section {
  padding-top: 1rem;
  padding-inline: 3rem;
  padding-bottom: 3rem;
}
.weather {
  grid-area: weather-section;
  display: grid;
  grid-template-rows: min-content min-content auto;
  grid-template-columns: repeat(6, 1fr);
  grid-template-areas:
    "jumbo jumbo jumbo jumbo jumbo jumbo"
    "search search search button button button"
    "weather weather weather weather weather weather"
    ;
  grid-row-gap: 1rem;
  align-items: center;
  justify-content: space-around;
  background-color: rgb(16, 5, 41);
}

.search {
  grid-area: search;
  justify-self: right;
  display: flex;
  justify-content: right;
  width: 100%;
}

.location {
  grid-area: button;
  justify-self: left;
  display: flex;
  justify-content: left;
  width: 100%;
  button {
    font-size: 1rem;
    padding: 5px;
    font-weight: bolder;
    margin-left: 2rem;
  }
}
.weather-bar {
  grid-area: weather;
  display: grid;
  grid-template-rows: min-content min-content;
  grid-template-columns: 1fr 2fr;
  grid-template-areas:
    "widget forecast forecast"
    "widget describe describe"
  ;
  column-gap: 1rem;
  justify-content: space-around;
  align-items: flex-start;
  padding-top: 1rem;
}
.current-weather {
  grid-area: widget;
  display: grid;
  grid-template:
    [row1-start] "weather-widget" auto [row1-end]
    [row2-start] "action-call" min-content [row2-end]
    [row3-start] "button-action" min-content [row3-end]
    / auto
  ;
  text-align: center;
  align-items: center;
  justify-content: center;
  margin-top: 2rem;
  button {
    font-size: 1rem;
    padding: 5px;
    font-weight: bolder;
    margin-inline: 1rem;
  }
}

.forecast {
  grid-area: forecast;
}

.description {
  grid-area: describe;
  p {
    text-align: center;
    font-size: .9rem;
  }
}

.subscription {
  grid-area: subscription-section;
  display: grid;
  grid-template-rows: min-content min-content;
  grid-template-columns: 50px 1fr 1fr 1fr 50px;
  grid-row-gap: 1rem;
  column-gap: 1.5rem;
  align-items: center;
  justify-content: space-around;
  width: 100%;
  color: var(--black);
  background-color: var(--brilliant-white);
  span > h1 {
    color: var(--navigation-bg);
  }
  .regular-user {
    grid-area: 2 / 2 / 3 / 2;
  }
  .farmer {
    grid-area: 2 / 3 / 3 / 4;
  }
  .organization {
    grid-area: 2 / 4 / 3 / 5;
  }
}
.organization, .farmer, .regular-user {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 20px;
}
h1 {
  color: var(--white);
  font-size: 56px;
}
input.search-bar {
  border: none;
  outline: none;
  border-radius: 24px;
  background: var(--bg-black);
  color: var(--white);
  font-family: inherit;
  margin-right: 1rem;
  padding-inline: 0.7rem;
}
.search-button {
  border-radius: 50%;
  display: flex;
  align-items: center;
  border: none;
  height: 32px;
  width: 35px;
  outline: none;
  background: var(--bg-black);
  color: var(--brilliant-white);
  cursor: pointer;
  transition: 0.2s ease-in-out;
}

.jumbotron1, .jumbotron2 {
  text-align: center;
  font-family: Georgia, 'Times New Roman', Times, serif;
}

.jumbotron1 {
  grid-area: jumbo;
}
.jumbotron2 {
  grid-area: 1 / 1 / 2 / end;
}
#casts {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  overflow-x: scroll;
  overflow-y: hidden;
  width: 100%;
  padding: .5rem;
  background-color: var(--component-bg);
  &::-webkit-scrollbar {
    height: 10px;
  }
  &::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  &::-webkit-scrollbar-thumb {
    background: var(--success);
    &:hover {
      background: rgb(13, 80, 10);
    }
  }
}
.columns {
  min-width: 380px;
}
.type {
  display: grid;
  grid-template-rows: min-content min-content min-content min-content;
  grid-template-columns: auto;
  width: 100%;
  height: 100%;
  align-items: flex-start;
  justify-content: center;
  border: 1px solid var(--component-bg);
  background-color: var(--component-bg);
  border-radius: 12px;
  .title {
    grid-area: 1 / 1 / 2 / 2;
    text-align: center;
    font-weight: bolder;
  }
  .illustrate {
    grid-area: 2 / 1 / 3 / 2;
    display: flex;
    justify-content: center;
    img {
      width: auto;
      height: 300px;
    }
  }
  .info {
    grid-area: 3 / 1 / 4 / 2;
    text-align: center;
    width: 100%;
    padding: 15px;
    font-size: 1.1rem;
  }
  .more {
    grid-area: 4 / 1 / 5 / 2;
    width: 70%;
    justify-self: center;
    font-size: 1.1rem;
    margin-bottom: 22px;
  }
}
@media all and (max-width: 540px) {
  .subscription, .current-weather, .weather, .weather-bar, .type, #home {
    grid-auto-flow: row dense;
  }
}
</style>

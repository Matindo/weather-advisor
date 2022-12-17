<template>
  <div id="home">
    <section class="weather">
      <span class="jumbotron1">
        <h1>Get current weather and forecasts from any location, any time</h1>
      </span>
      <div class="sub-jumbo">
        <div id="search-bar">
          <search-bar />
        </div>
        <div class="location">
          <b-button size="sm" variant="outline-light" pill @click="locationWeather()">Get Current Location's Weather</b-button>
        </div>
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
          <div class="description">
            <p>*this is a 3-hour weather forecast for five days, starting from the time you refresh or reload this page</p>
          </div>
        </div>
      </div>
    </section>
    <section class="subscription">
      <span class="jumbotron2">
        <h1>Subscribe to get customized weather messages and alerts</h1>
      </span>
      <div class="subscribers">
        <div class="regular-user">
          <div class="title">Regular User</div>
          <div class="illustrate"><img src="../assets/images/Push notifications-cuate.png" alt="regular" /></div>
          <div class="info">You'll get daily alerts on weather forecasts you want to help you plan your daily activities.</div>
          <b-button class="more p-0" size="sm" variant="outline-primary" @click="regularSubscribe">Subscribe</b-button>
        </div>
        <div class="farmer">
          <div class="title">Farmer</div>
          <div class="illustrate"><img src="../assets/images/Farmer-rafiki.png" alt="farmer" /></div>
          <div class="info">You'll get weekly and monthly forecasts and predictions to help you plan for your farm activities.</div>
          <b-button class="more p-0" size="sm" variant="outline-success" @click="farmerSubscribe">Subscribe</b-button>
        </div>
        <div class="organization">
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
    <b-modal ref="modal-login" hide-footer title="Login" hide-header-close>
      <b-form @submit.prevent="signIn" @reset="resetLogin" v-show="show">
        <b-form-row class="w-100">
          <b-form-group id="email" label="Email:" label-for="input-email">
            <b-form-input id="input-email" v-model="formData.email" type="email" required trim></b-form-input>
          </b-form-group>
        </b-form-row>
        <b-form-row class="w-100">
          <b-form-group id="pword" label="Password:" label-for="input-pword">
            <b-form-input id="input-pword" v-model="formData.pass" type="password" required></b-form-input>
          </b-form-group>
        </b-form-row>
        <div class="form-footer w-100">
          <b-button class="mx-2" type="submit" variant="primary">Sign In</b-button>
          <b-button class="mx-2" type="reset" variant="warning">Reset</b-button>
          <b-button class="mx-2" type="close" variant="danger" @click="closeLogin">Cancel</b-button>
        </div>
      </b-form>
    </b-modal>
    <snack-bar :message="barMessage" :variant="status"/>
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue'
import SearchBar from '@/components/SearchBar.vue'
import WeatherWidget from '../components/WeatherWidget.vue'
import { locationMixin } from '@/mixins/locationMixin'
import { weatherMixin } from '@/mixins/weatherMixin'
import ForecastWidget from '@/components/ForecastWidget.vue'
import { mapGetters } from 'vuex'
import SnackBar from '@/components/SnackBar.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: { RegisterForm, WeatherWidget, ForecastWidget, SnackBar, SearchBar },
  mixins: [locationMixin, weatherMixin],
  data: function () {
    return {
      formOptions: { userType: 'Regular' },
      formData: {
        email: '', pass: ''
      },
      show: true
    }
  },
  computed: {
    ...mapGetters({
      city: 'CITY',
      location: 'LOCATION',
      barMessage: 'MESSAGE',
      status: 'STATUS'
    })
  },
  methods: {
    search: function (searchQuery) {
      this.fetchCityWeather(searchQuery)
      this.fetchCityForecast(searchQuery)
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
      this.formOptions.userType = 'Farmer'
      this.showSubscribeModal()
    },
    orgSubscribe: function () {
      this.formOptions.userType = 'Organization'
      this.showSubscribeModal()
    },
    showSnackbar: function () {
      document.getElementById('snackbar').className = 'show'
    },
    showLoginModal: function () {
      this.$refs['modal-login'].show()
    },
    closeLogin: function () {
      this.$refs['modal-login'].hide()
    },
    signIn: function () {
      const formData = new FormData()
      formData.append('email', this.formData.email)
      formData.append('pword', this.formData.pass)
      axios({
        method: 'POST',
        url: './api/Subscribe.php?action=login',
        data: formData,
        headers: { 'Content-Type': 'multipart/form-data' }
      }).then(res => {
        if (res.data.error) {
          this.$store.dispatch('SET_STATUS', 'danger')
          this.$store.dispatch('SET_MESSAGE', res.data.message)
          return
        }
        this.$store.dispatch('SET_STATUS', 'success')
        this.$store.dispatch('SET_MESSAGE', res.data.message)
      }).finally(() => {
        this.$root.$emit('showSnackbar')
        this.$router.push('/profile')
      })
    },
    resetLogin: function () {
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  },
  mounted: function () {
    let query = ''
    if (this.city !== '') {
      query = this.city
      this.fetchCityWeather(query)
      this.fetchCityForecast(query)
    } else if (this.location.length > 0) {
      this.fetchCoordinateWeather({ lon: this.location[0], lat: this.location[1] })
      this.fetchCoordinateForecast({ lon: this.location[0], lat: this.location[1] })
    } else {
      query = 'Nairobi'
      this.fetchCityWeather(query)
      this.fetchCityForecast(query)
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
    this.$root.$on('headerLogin', () => {
      this.showLoginModal()
    })
    this.$root.$on('searchbarSearch', (searchQuery) => {
      this.search(searchQuery)
    })
  }
}
</script>

<style lang="scss" scoped>
* {
  box-sizing: border-box;
  font-size: 1.5rem;
}
h1 {
  color: var(--white);
  font-size: 56px;
}
section {
  padding-top: 1rem;
  padding-inline: 3rem;
  padding-bottom: 3rem;
  width: 100%;
}
#home {
  display: grid;
  grid-template:
    [row1-start] "weather-section" min-content [row1-end]
    [row2-start] "subscription-section" min-content [row2-end]
    / auto
  ;
  align-items: center;
  justify-content: center;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}

.weather {
  grid-area: weather-section;
  display: grid;
  grid-template:
    [row1-start] "jumbo" min-content [row1-end]
    [row2-start] "sub-jumbo" min-content [row2-end]
    [row3-start] "weather" min-content [row3-end]
    / auto
  ;
  gap: 1rem;
  align-items: center;
  justify-content: space-around;
  background-color: rgb(16, 5, 41);
  width: 100%;
}
.jumbotron1 {
  grid-area: jumbo;
}
.sub-jumbo {
  grid-area: sub-jumbo;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-around;
  justify-self: center;
  width: 70%;
}
#search-bar {
  width: 50%;
}
.location {
  display: grid;
  grid-template-columns: minmax(400px, auto);
  grid-template-rows: min-content;
  justify-content: center;
  width: 50%;
  button {
    font-size: 1rem;
    padding: 5px;
    font-weight: bolder;
    margin-left: 2rem;
  }
}
.weather-bar {
  grid-area: weather;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: flex-start;
  padding-top: 1rem;
  width: 100%;
}
.current-weather {
  display: grid;
  grid-template:
    [row1-start] "weather-widget" min-content [row1-end]
    [row2-start] "action-call" min-content [row2-end]
    [row3-start] "button-action" min-content [row3-end]
    / auto
  ;
  text-align: center;
  align-items: center;
  justify-content: center;
  width: 40%;
  margin-top: 2rem;
  button {
    font-size: 1rem;
    padding: 5px;
    font-weight: bolder;
    margin-inline: 1rem;
  }
}
.forecast {
  display: grid;
  grid-template:
    [row1-start]"week-forecast" min-content[row1-end]
    [row2-start]"describe" min-content[row2-end]
    / auto
  ;
  width: 60%;
}
#week-forecast {
  grid-area: week-forecast;
  display: grid;
  width: 100%;
  #casts {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    overflow-x: scroll;
    overflow-y: hidden;
    padding: .5rem;
    background-color: var(--component-bg);
    .columns {
      min-width: 380px;
    }
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
  grid-template:
    [row1-start]"jumbo-line" min-content[row1-end]
    [row2-start]"subscribers" min-content[row2-end]
    / auto
  ;
  gap: 1rem;
  align-items: center;
  justify-content: space-around;
  width: 100%;
  color: var(--black);
  background-color: var(--brilliant-white);
}
.jumbotron2 {
  grid-area: jumbo-line;
  h1 {
    color: var(--black);
  }
}
.jumbotron1, .jumbotron2 {
  text-align: center;
  font-family: Georgia, 'Times New Roman', Times, serif;
}
.subscribers {
  grid-area: subscribers;
  display: grid;
  padding-inline: 3rem;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: min-content;
  column-gap: 1.5rem;
  grid-auto-flow: row dense;
}
.organization, .farmer, .regular-user {
  display: grid;
  grid-template:
    [row1-start]"title" min-content[row1-end]
    [row2-start]"illustrate" min-content[row2-end]
    [row3-start]"info" min-content[row3-end]
    [row4-start]"more" min-content[row4-end]
    / auto
  ;
  align-items: flex-start;
  justify-content: center;
  width: 100%;
  border-radius: 20px;
  padding: 30px;
  border: 1px solid var(--component-bg);
  background-color: var(--component-bg);
  .title {
    grid-area: title;
    text-align: center;
    font-weight: bolder;
  }
  .illustrate {
    grid-area: illustrate;
    display: flex;
    justify-content: center;
    img {
      width: 100%;
      height: auto;
      object-fit: contain;
      aspect-ratio: 1.5;
    }
  }
  .info {
    grid-area: info;
    text-align: center;
    width: 100%;
    padding: 15px;
    font-size: 1.1rem;
  }
  .more {
    grid-area: more;
    width: 70%;
    justify-self: center;
    font-size: 1.1rem;
    margin-bottom: 22px;
  }
}

@media all and (max-width: 900px) {
  .subscribers {
    padding-inline: 1rem;
    grid-template-columns: auto;
    gap: 1.5rem;
  }
  .organization, .farmer, .regular-user {
    margin-inline: 1rem;
  }
  .sub-jumbo {
    width: 100%;
    justify-content: space-evenly;
  }
  .current-weather { width: 100%; }
  .forecast { width: 100%; margin-top: 9px; }
  #search-bar { width: 60%; }
}
</style>

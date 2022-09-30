<template>
  <b-container id="forecasts" fluid>
    <div class="search">
      <input type="text" class="search-bar" placeholder="Search" v-model="searchQuery" @keyup.enter="search()" />
      <button class="search-button" @click="search()">
        <b-icon icon="search"></b-icon>
      </button>
      <b-button class="weather-getter" variant="outline-success" pill @click="locationWeather()">Get Current Location's Weather</b-button>
    </div>
    <b-row class="carrd">
      <b-col id="current-weather" cols="12" md="6" lg="4">
        <WeatherWidget :weatherDetails="weatherData"></WeatherWidget>
        <b-row class="default mt-1" align-h="center" align-v="center">
          <b-col cols="12">
            <p style="text-align:justify;">Do you want to set this location as your default location for weather data and forecasts whenever you load this site?
            </p>
          </b-col>
          <b-col cols="12" md="8">
            <b-button pill variant="outline-primary" @click="setDefaultWeatherLocation">Yes, Set Default Location</b-button>
          </b-col>
        </b-row>
      </b-col>
      <b-col id="forecast-weather" cols="12" md="6" lg="8">
        <div id="week-forecast">
          <h2>This week's forecast: </h2>
          <div id="casts">
            <b-col v-for="forecast in weatherForecast" :key="forecast.day" class="mx-2 columns">
              <ForecastWidget  :forecast="forecast" />
            </b-col>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import WeatherWidget from '../components/WeatherWidget.vue'
import { locationMixin } from '@/mixins/locationMixin'
import { weatherMixin } from '@/mixins/weatherMixin'
import ForecastWidget from '@/components/ForecastWidget.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'ForecastsView',
  components: { WeatherWidget, ForecastWidget },
  mixins: [locationMixin, weatherMixin],
  computed: {
    ...mapGetters({
      city: 'CITY',
      location: 'LOCATION'
    })
  },
  data: function () {
    return {
      searchQuery: ''
    }
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
    document.getElementById('forecasts').style.backgroundImage = 'linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url(\'https://source.unsplash.com/1600x900/?weather\')'
    this.details = this.weatherData
  }
}
</script>

<style lang="scss" scoped>
#forecasts {
  color: var(--white);
  padding: 2em;
  width: 100%;
  height: 120vh;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
.search {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  width: 100%;
}
.search-button {
  margin: 0.5em;
  border-radius: 50%;
  border: none;
  height: 44px;
  width: 44px;
  outline: none;
  background: var(--bg-black);
  color: var(--brilliant-white);
  cursor: pointer;
  transition: 0.2s ease-in-out;
}
input.search-bar {
  border: none;
  outline: none;
  padding: 0.4em 1em;
  border-radius: 24px;
  background: var(--bg-black);
  color: var(--white);
  font-family: inherit;
  font-size: 105%;
}
button:hover {
  background: var(--hover-grey);
  color: var(--black);
}
.carrd {
  background: var(--bg-black);
  color: var(--white);
  padding: 2em;
  border-radius: 30px;
  width: 100%;
  margin: 1em;
  display: flex;
  justify-content: left;
  align-items: center;
  flex-wrap: nowrap;
}
.weather-getter {
  margin-left: 1rem;
}
#forecast-weather {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  * {
    width: 100%;
  }
}
#week-forecast {
  width: 100%;
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
  margin: 5px .2rem 10px .2rem;
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
@media all and (max-width: 768px){
  .carrd {
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    overflow-y: auto;
    ::-webkit-scrollbar {
      visibility: hidden;
    }
  }
}
</style>

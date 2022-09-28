<template>
  <b-container id="forecasts" fluid>
    <div class="search">
      <input type="text" class="search-bar" placeholder="Search" v-model="searchQuery" @keyup.enter="search()" />
      <button class="search-button" @click="search()">
        <b-icon icon="search"></b-icon>
      </button>
      <b-button class="weather-getter" variant="outline-success" pill @click="locationWeather()">Get Current Location's Weather</b-button>
    </div>
    <b-row class="card">
      <b-col id="current-weather" cols="12" md="6" lg="4">
        <WeatherWidget :weatherDetails="weatherData"></WeatherWidget>
      </b-col>
      <b-col id="forecast-weather">
        <b-row id="day-forcast">
          <h3>The rest of the day...</h3>
        </b-row>
        <b-row id="week-forecast">
          <h3>The rest of the week...</h3>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import WeatherWidget from '../components/WeatherWidget.vue'
import { locationMixin } from '@/mixins/locationMixin'
import { weatherMixin } from '@/mixins/weatherMixin'

export default {
  name: 'ForecastsView',
  components: { WeatherWidget },
  mixins: [locationMixin, weatherMixin],
  data: function () {
    return {
      searchQuery: ''
    }
  },
  methods: {
    search: function () {
      this.fetchCityWeather(this.searchQuery)
    },
    locationWeather: function () {
      this.getLocation()
      if (!this.error) {
        this.fetchCoordinateWeather({ lon: this.longitude, lat: this.lattitude })
      } else {
        // show toast message with error
      }
    }
  },
  mounted: function () {
    this.fetchCityWeather('Nairobi')
    document.getElementById('forecasts').style.backgroundImage = 'linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url(\'https://source.unsplash.com/1600x900/?weather\')'
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
.card {
  background: var(--bg-black);
  color: var(--white);
  padding: 2em;
  border-radius: 30px;
  width: 100%;
  margin: 1em;
  display: flex;
  justify-content: space-around;
  align-items: stretch;
  flex-wrap: wrap;
  * {
    border: 1px solid blue;
  }
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

@media all and (max-width: 548px){
  .card { align-items: center; }
  .day-forecast, .week-forecast {
    overflow-x: scroll;
  }
}
</style>

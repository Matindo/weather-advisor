<template>
  <b-container id="forecasts" fluid>
    <div class="search">
      <input type="text" class="search-bar" placeholder="Search" v-model="searchQuery" />
      <button @click="search()" @keyup.enter="search()">
        <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" height="1.5em" width="1em" xmlns="http://www.w3.org/2000/svg">
          <path d="M505.04 442.66l-99.71-99.69c-4.5-4.5-10.6-7-17-7h-16.3c27.6-35.3 44-79.69 44-127.99C416.03 93.09 322.92 0 208.02 0S0 93.09 0 207.98s93.11 207.98 208.02 207.98c48.3 0 92.71-16.4 128.01-44v16.3c0 6.4 2.5 12.5 7 17l99.71 99.69c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.59.1-33.99zm-297.02-90.7c-79.54 0-144-64.34-144-143.98 0-79.53 64.35-143.98 144-143.98 79.54 0 144 64.34 144 143.98 0 79.53-64.35 143.98-144 143.98zm.02-239.96c-40.78 0-73.84 33.05-73.84 73.83 0 32.96 48.26 93.05 66.75 114.86a9.24 9.24 0 0 0 14.18 0c18.49-21.81 66.75-81.89 66.75-114.86 0-40.78-33.06-73.83-73.84-73.83zm0 96c-13.26 0-24-10.75-24-24 0-13.26 10.75-24 24-24s24 10.74 24 24c0 13.25-10.75 24-24 24z"></path>
        </svg>
      </button>
    </div>
    <div class="card">
      <WeatherWidget :weatherDetails="weatherData"></WeatherWidget>
    </div>
  </b-container>
</template>

<script>
import WeatherWidget from '../components/WeatherWidget.vue'
export default {
  name: 'ForecastsView',
  components: { WeatherWidget },
  data: function () {
    return {
      searchQuery: '',
      apiKey: 'ed0b2d87cc61572f8ae096b3700e8d28',
      weatherData: {
        city: '', icon: '', description: '', temp: '', humidity: '', wind: '', status: ''
      }
    }
  },
  methods: {
    fetchWeather: function (city) {
      fetch('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + this.apiKey).then((response) => response.json()).then((data) => {
        this.displayWeather(data)
      })
    },
    displayWeather: function (data) {
      const { name } = data
      const { icon, description } = data.weather[0]
      const { temp, humidity } = data.main
      const { speed } = data.wind
      this.weatherData.city = 'Weather in ' + name
      this.weatherData.icon = 'https://openweathermap.org/img/wn/' + icon + '.png'
      this.weatherData.description = description
      this.weatherData.temp = temp + '⁰C'
      this.weatherData.humidity = 'Humidity: ' + humidity + '%'
      this.weatherData.wind = 'Wind Speed: ' + speed + 'km/h'
      this.weatherData.status = 'ready'
      document.getElementById('forecasts').style.backgroundImage = `linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url('https://source.unsplash.com/1600x900/?${name}')`
    },
    search: function () {
      this.fetchWeather(this.searchQuery)
    }
  },
  mounted: function () {
    this.fetchWeather('Nairobi')
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
  width: 100%;
}
button {
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
  max-width: 420px;
  margin: 1em;
}
</style>

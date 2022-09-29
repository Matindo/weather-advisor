<template>
  <div id="weather-widget">
    <div id="no-data" v-if="loadingText">
      <div id="loading">
        <b-icon icon="arrow-clockwise" animation="spin" font-scale="4"></b-icon>
        <h3>Loading data</h3>
      </div>
    </div>
    <div class="weather" v-else>
      <h2 class="city">{{ weatherDetails.city }}</h2>
      <h1 class="temp">{{ weatherDetails.temp }}</h1>
      <div class="flex">
        <img :src="weatherDetails.icon" alt="weather-icon" class="icon" />
        <div class="description">{{ weatherDetails.description }}</div>
      </div>
      <div class="humidity">{{ weatherDetails.humidity }}</div>
      <div class="wind">{{ weatherDetails.wind }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WeatherWidget',
  props: {
    weatherDetails: {
      type: Object,
      required: true
    }
  },
  computed: {
    loadingText: function () {
      if (this.weatherDetails.status === 'ready') {
        document.getElementById('weather-widget').style.backgroundImage = `linear-gradient(to bottom, rgba(34, 34, 34, .5), rgba(5, 5, 5, .5)),url('https://source.unsplash.com/1600x900/?${this.weatherDetails.background}')`
        return false
      } else {
        return true
      }
    }
  }
}
</script>

<style lang="scss" scoped>
#weather-widget {
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  color: inherit;
  padding: .9rem;
  border-radius: 15px;
}
h1.temp {
  margin: 0;
  margin-bottom: 0.5em;
}
.flex {
  display: flex;
  align-items: center;
}
.description {
  text-transform: capitalize;
  margin-left: 8px;
}
.no-data, .loading {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.loading {
  flex-direction: column;
}
</style>

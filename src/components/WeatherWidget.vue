<template>
  <div class="weather" :class="loadingText ? 'loading' : 'show'">
    <h2 class="city">{{ weatherDetails.city }}</h2>
    <h1 class="temp">{{ weatherDetails.temp }}</h1>
    <div class="flex">
      <img :src="weatherDetails.icon" alt="weather-icon" class="icon" />
      <div class="description">{{ weatherDetails.description }}</div>
    </div>
    <div class="humidity">{{ weatherDetails.humidity }}</div>
    <div class="wind">{{ weatherDetails.wind }}</div>
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
        return false
      } else {
        return true
      }
    }
  },
  mounted: function () {
    console.log(this.weatherDetails)
  }
}
</script>

<style lang="scss" scoped>
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
.weather {
  visibility: hidden;
  max-height: 20px;
  position: relative;
}
.weather.show {
  visibility: visible;
  max-height:max-content;
}
.weather.loading:after {
  visibility: visible;
  content: "Loading...";
  color: var(--white);
  position: absolute;
  top: 0;
  left: 20px;
}
</style>

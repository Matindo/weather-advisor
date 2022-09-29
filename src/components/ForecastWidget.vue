<template>
  <div id="forecast-widget" class="mx-2">
    <div class="date">{{forecast.date}}</div>
    <div class="time early" v-if="weathers.early.icon !== ''">
      <p>06:00AM:</p>
      <p>{{ weathers.early.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.early.icon}.png`" alt="icon" class="icon" /> {{ weathers.early.weather }}</p>
    </div>
    <div class="time morning" v-if="weathers.morning.icon !== ''">
      <p>09:00AM:</p>
      <p>{{ weathers.morning.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.morning.icon}.png`" alt="icon" class="icon" /> {{ weathers.morning.weather }}</p>
    </div>
    <div class="time noon" v-if="weathers.noon.icon !== ''">
      <p>12:00PM:</p>
      <p>{{ weathers.noon.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.noon.icon}.png`" alt="icon" class="icon" /> {{ weathers.noon.weather }}</p>
    </div>
    <div class="time noon" v-if="weathers.afternoon.icon !== ''">
      <p>15:00PM:</p>
      <p>{{ weathers.afternoon.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.afternoon.icon}.png`" alt="icon" class="icon" /> {{ weathers.afternoon.weather }}</p>
    </div>
    <div class="time evening" v-if="weathers.evening.icon !== ''">
      <p>18:00PM:</p>
      <p>{{ weathers.evening.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.evening.icon}.png`" alt="icon" class="icon" /> {{ weathers.evening.weather }}</p>
    </div>
    <div class="time night" v-if="weathers.night.icon !== ''">
      <p>21:00PM: </p>
      <p>{{ weathers.night.temp + '⁰C'}}</p>
      <p class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.night.icon}.png`" alt="icon" class="icon" /> {{ weathers.night.weather }}</p>
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ForecastWidget',
  props: {
    forecast: {
      type: Object,
      required: true
    }
  },
  computed: {
  },
  data: function () {
    return {
      weathers: {
        early: { weather: '', icon: '', temp: null },
        morning: { weather: '', icon: '', temp: null },
        noon: { weather: '', icon: '', temp: null },
        afternoon: { weather: '', icon: '', temp: null },
        evening: { weather: '', icon: '', temp: null },
        night: { weather: '', icon: '', temp: null }
      }
    }
  },
  methods: {
    splitWeathers: function () {
      const weatherz = this.forecast.weather
      for (let i = 0; i < 8; i++) {
        const date = moment(weatherz[i].dt_txt).format('L')
        if (date === this.forecast.date) {
          const time = this.timeOfDay(weatherz[i].dt_txt)
          const def = weatherz[i].weather[0]
          if (time === 'early') {
            this.weathers.early = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          } else if (time === 'morning') {
            this.weathers.morning = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          } else if (time === 'noon') {
            this.weathers.noon = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          } else if (time === 'afternoon') {
            this.weathers.afternoon = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          } else if (time === 'evening') {
            this.weathers.evening = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          } else if (time === 'night') {
            this.weathers.night = { weather: def.description, icon: def.icon, temp: weatherz[i].main.temp }
          }
        }
      }
    },
    timeOfDay: function (date) {
      const hour = moment(date).hour()
      if (hour === 6) {
        return 'early'
      } else if (hour === 9) {
        return 'morning'
      } else if (hour === 12) {
        return 'noon'
      } else if (hour === 15) {
        return 'afternoon'
      } else if (hour === 18) {
        return 'evening'
      } else if (hour === 21) {
        return 'night'
      }
    }
  },
  mounted: function () {
    this.splitWeathers()
  }
}
</script>

<style lang="scss" scoped>
#forecast-widget {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-width: max-content;
  width: 250px;
}
.time {
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  padding: .2rem .1rem;
  width: 100%;
  display: flex;
  justify-content: left;
  align-items: center;
  flex-direction: row;
  .desc {
    text-transform: capitalize;
  }
}
.early {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .25), rgba(5, 5, 5, .4)), url('../assets/images/mountain-magic-hour.jpg');
}
.morning {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .3), rgba(5, 5, 5, .5)), url('../assets/images/cloud-wrapped-mountain.jpg');
}
.noon {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .3), rgba(5, 5, 5, .5)), url('../assets/images/humberto-arellano-vh_gSEGcbhk-unsplash.jpg');
}
.afternoon {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .3), rgba(5, 5, 5, .5)), url('../assets/images/puppy-at-the-beach.jpg');
}
.evening {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .25), rgba(5, 5, 5, .4)), url('../assets/images/african-safari-sunset.jpg');
}
.night {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .2), rgba(5, 5, 5, .3)), url('../assets/images/a-view-of-the-stars-on-night-sky.jpg');
}
</style>

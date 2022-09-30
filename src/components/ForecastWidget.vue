<template>
  <div id="forecast-widget" class="mx-2 container">
    <b-row class="date"><h4>{{weekday}}</h4></b-row>
    <b-row class="early w-100" v-if="weathers.early.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">0600h</b-col>
      <b-col cols="7" class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.early.icon}.png`" alt="icon" class="icon" /> {{ weathers.early.weather }}</b-col>
      <b-col cols="3"> {{weathers.early.temp + '⁰C'}}</b-col>
    </b-row>
    <b-row class="morning w-100" v-if="weathers.morning.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">0900h</b-col>
      <b-col cols="7" class="desc"><img :src="`https://openweathermap.org/img/wn/${weathers.morning.icon}.png`" alt="icon" class="icon" /> {{ weathers.morning.weather }}</b-col>
      <b-col cols="3">{{ weathers.morning.temp + '⁰C'}}</b-col>
    </b-row>
    <b-row class="noon w-100" v-if="weathers.noon.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">1200h</b-col>
      <b-col class="desc" cols="7"><img :src="`https://openweathermap.org/img/wn/${weathers.noon.icon}.png`" alt="icon" class="icon" /> {{ weathers.noon.weather }}</b-col>
      <b-col cols="3">{{ weathers.noon.temp + '⁰C'}}</b-col>
    </b-row>
    <b-row class="noon w-100" v-if="weathers.afternoon.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">1500h</b-col>
      <b-col class="desc" cols="7"><img :src="`https://openweathermap.org/img/wn/${weathers.afternoon.icon}.png`" alt="icon" class="icon" /> {{ weathers.afternoon.weather }}</b-col>
      <b-col cols="3">{{ weathers.afternoon.temp + '⁰C'}}</b-col>
    </b-row>
    <b-row class="evening w-100" v-if="weathers.evening.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">1800h </b-col>
      <b-col class="desc" cols="7"><img :src="`https://openweathermap.org/img/wn/${weathers.evening.icon}.png`" alt="icon" class="icon" /> {{ weathers.evening.weather }}</b-col>
      <b-col cols="3">{{ weathers.evening.temp + '⁰C'}}</b-col>
    </b-row>
    <b-row class="night w-100" v-if="weathers.night.icon !== ''" align-v="center" align-h="between">
      <b-col cols="2">2100h </b-col>
      <b-col class="desc" cols="7"><img :src="`https://openweathermap.org/img/wn/${weathers.night.icon}.png`" alt="icon" class="icon" /> {{ weathers.night.weather }}</b-col>
      <b-col cols="3">{{ weathers.night.temp + '⁰C'}}</b-col>
    </b-row>
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
    weekday: function () {
      return moment(this.forecast.date).format('dddd')
    }
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
  flex-direction: column;
  border-radius: 20px;
}
.desc {
  text-transform: capitalize;
}
.early {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .25), rgba(5, 5, 5, .4)), url('../assets/images/jenna-lee-zFk1FdVSlOs-unsplash.jpg');
}
.morning {
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .3), rgba(5, 5, 5, .5)), url('../assets/images/hendrik-kespohl-UPnxtRNH8q8-unsplash.jpg');
  background-position-y: center;
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

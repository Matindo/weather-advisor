<template>
  <div id="forecast-widget">
    <div class="date">{{forecast.date}}</div>
    <div class="early"></div>
    <div class="morning"></div>
    <div class="noon"></div>
    <div class="evening"></div>
    <div class="night"></div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ForecastWidget',
  prop: {
    forecast: {
      type: Object,
      required: true
    }
  },
  computed: {
    timeOfDay: function (date) {
      const hour = moment(date).hour()
      if (hour === 6) {
        return 'early'
      } else if(hour === 9) {
        return 'morning'
      } else if (hour === 12) {
        return 'noon'
      } else if (hour === 18) {
        return 'evening'
      } else if (hour === 21 ) {
        return 'night'
      }
    }
  },
  data: function () {
    return {
      times: []
    }
  }
}
</script>

<style lang="scss" scoped>
#forecast-widget {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 6rem;
  * {
    width: 100%;
    height: 4rem;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
}
</style>

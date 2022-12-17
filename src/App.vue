<template>
  <div id="app">
    <Navbar />
    <router-view/>
    <FootSection />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import FootSection from './components/FootSection.vue'

export default {
  components: { Navbar, FootSection },
  computed: {
    daytime: function () {
      var currentHour = new Date().getHours()
      var timeOfDay = ''
      console.log(currentHour)
      if (currentHour >= 19 || currentHour < 6) {
        timeOfDay = 'night'
      } else if (currentHour >= 6 && currentHour < 9) {
        timeOfDay = 'morning'
      } else if (currentHour >= 9 && currentHour < 12) {
        timeOfDay = 'mid-morning'
      } else if (currentHour >= 12 && currentHour < 15) {
        timeOfDay = 'midday'
      } else if (currentHour >= 14 && currentHour < 16) {
        timeOfDay = 'afternoon'
      } else if (currentHour >= 16 && currentHour < 19) {
        timeOfDay = 'evening'
      }
      return timeOfDay
    }
  },
  created: function () {
    this.$store.dispatch('READ_DEFAULT_CITY')
    this.$store.dispatch('READ_DEFAULT_LOCATION')
  },
  mounted: function () {
    document.getElementById('app').style.backgroundImage = `linear-gradient(to bottom, rgba(34, 34, 34, .05), rgba(5, 5, 5, .15)),url('https://source.unsplash.com/1600x900/?${this.daytime}')`
  }
}
</script>

<style lang="scss">
:root {
  --primary: #592f04;
  --success: #1e790a;
  --black: #050404;
  --bg-black: #000000d0;
  --section-black: #333;
  --component-bg: #7c7c7c2b;
  --white: #e0e0e0;
  --brilliant-white: #ffffff;
  --hover-grey: #7c7c7c6b;
  --header-bg: rgba(34, 34, 34, 0.87);
  --navigator-bg: rgba(10, 9, 7, 0.945);
  transition: all .5s ease-in-out;
}

#app {
  background-size: cover;
  background-attachment: fixed;
  color: var(--white);
}
</style>

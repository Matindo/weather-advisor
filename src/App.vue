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
  created: function () {
    this.$store.dispatch('READ_DEFAULT_CITY')
    this.$store.dispatch('READ_DEFAULT_LOCATION')
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
}

#app {
  background-image: linear-gradient(to bottom, var(--header-bg), rgba(34, 34, 34, 0.952)), url('./assets/images/a-view-of-the-stars-on-night-sky.jpg');
  background-size: cover;
  background-attachment: fixed;
  color: var(--white);
}
</style>

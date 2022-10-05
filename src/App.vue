<template>
  <div id="app">
    <div class="topdiv">
      <div class="headline">
        <img src="./assets/images/logo.png" alt="logo" width="64" height="64" />
        <h1>MISIMU</h1>
      </div>
      <div class="tagline">
        <h5>Your One-stop Weather Advisor</h5>
      </div>
    </div>
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
  data: function () {
    return {
      showNavbar: true,
      lastScrollPosition: 0
    }
  },
  methods: {
    onScroll () {
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
      if (currentScrollPosition < 0) {
        return
      }
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 30) {
        return
      }
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      // Set the current scroll position as the last scroll position
      this.lastScrollPosition = currentScrollPosition
    }
  },
  created: function () {
    this.$store.dispatch('READ_DEFAULT_CITY')
    this.$store.dispatch('READ_DEFAULT_LOCATION')
  },
  mounted: function () {
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy: function () {
    window.removeEventListener('scroll', this.onScroll)
  }
}
</script>

<style lang="scss">
:root {
  --primary: #592f04;
  --success: #1e790a;
  --black: #050404;
  --bg-black: #000000d0;
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
.topdiv {
  display: flex;
  justify-content: center;
  flex-direction: column;
  width: 100vw;
  h1, h2, h3, h4, h5, h6 {
    margin-bottom: 0;
  }
}
.headline {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-end;
  text-align: center;
  width: 100%;
}
.tagline {
  display: inline;
  text-align: center;
  width: 100%;
}
</style>

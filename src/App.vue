<template>
  <div id="app">
    <Navbar />
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  components: { Navbar },
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
}

#app {
  background: var(--black);
  color: var(--white);
}
</style>

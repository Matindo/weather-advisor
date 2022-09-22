<template>
  <div id="app">
    <div class="logo">
      <h1>Misimu</h1>
    </div>
    <Navbar />
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  components: { Navbar }
}
</script>

<style lang="scss">
.logo {
  width: 100vw;
  display: flex;
  align-content: center;
  justify-content: center;
  background-image: url('./assets/images/mountain-magic-hour.jpg');
  background-position-x: center;
  background-position-y: top;
  background-repeat: no-repeat;
  color: white;
  h1 {
    font-size: 5rem;
  }
}
</style>

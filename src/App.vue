<template>
  <div id="app">
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
:root {
  --primary: #592f04;
  --success: #1e790a;
  --black: #050404;
  --white: #e0e0e0;
}

#app {
  background: var(--black);
  color: var(--white);
}
</style>

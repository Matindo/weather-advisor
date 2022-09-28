<template>
  <b-container fluid id="ngos"></b-container>
</template>

<script>
export default {
  name: 'NGOsView',
  mounted: function () {
    document.getElementById('ngos').style.backgroundImage = 'linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url(\'https://source.unsplash.com/1600x900/?NGO\')'
  }
}
</script>

<style lang="scss" scoped>
#ngos {
  width: 100%;
  height: 120vh;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
</style>

<template>
  <b-container fluid id="accounts"></b-container>
</template>

<script>
export default {
  name: 'AccountsView',
  mounted: function () {
    document.getElementById('accounts').style.backgroundImage = 'linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url(\'https://source.unsplash.com/1600x900/?weather\')'
  }
}
</script>

<style lang="scss" scoped>
#accounts {
  width: 100%;
  height: 102vh;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
</style>

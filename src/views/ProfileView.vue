<template>
  <div id="account"></div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters({
      user: 'USER'
    })
  }
}
</script>

<style lang="scss" scoped>
#account {
  width: 100%;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: auto;
  justify-content: center;
  align-items: center;
}
</style>

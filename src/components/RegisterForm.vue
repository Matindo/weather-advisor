<template>
  <div id="register-form">
    <b-form @submit.prevent="submit()" @reset="reset()" v-show="show"></b-form>
  </div>
</template>

<script>
export default {
  name: 'RegisterForm',
  data: function () {
    return {
      show: true
    }
  },
  methods: {
    submit: function () {
      // gather data and send to server
    },
    reset: function () {
      // reset form data
      this.$nextTick(() => {
        this.show = false
      })
      this.show = true
    }
  }
}
</script>

<style lang="scss" scoped>
</style>

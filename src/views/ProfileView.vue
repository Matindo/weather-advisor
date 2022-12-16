<template>
  <div id="account">
    <div class="user-item" v-if="!user.fname">
      <b-form-group label="First Name: " label-for="fname">
        <b-form-input id="fname" type="text" disabled v-model="user.fname" />
      </b-form-group>
    </div>
    <div class="user-item" v-if="!user.lname">
      <b-form-group label="Other Name: " label-for="lname">
        <b-form-input id="lname" type="text" disabled v-model="user.lname" />
      </b-form-group>
    </div>
    <div class="user-item" v-if="!user.email">
      <b-form-group label="Email: " label-for="email">
        <b-form-input id="email" type="text" disabled v-model="user.email" />
      </b-form-group>
    </div>
    <div class="user-item" v-if="!user.phone">
      <b-form-group label="First Name: " label-for="mobile">
        <b-form-input id="mobile" type="text" disabled value="user.phone" />
      </b-form-group>
    </div>
    <div class="button-section w-100">
      <b-button variant="outline-success" pill @click="updateDetails">Update Details</b-button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters({
      user: 'USER'
    })
  },
  methods: {
    updateDetails: function () {
      const formData = new FormData()
      // formData.append()
      axios({
        method: 'POST',
        url: 'api/Subscribe.php?action=update',
        data: formData,
        headers: { 'Content-Type': 'multipart/form-data' }
      }).then(res => {
        if (res.data.error) {
          this.$store.dispatch('SET_STATUS', 'danger')
          this.$store.dispatch('SET_MESSAGE', res.data.message)
          return
        }
        this.$store.dispatch('SET_STATUS', 'success')
        this.$store.dispatch('SET_MESSAGE', res.data.message)
      }).finally(() => {
        this.$root.$emit('showSnackbar')
        this.$router.push('/profile')
      })
    }
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
  gap: 1rem;
  margin: 0 auto;
}

@media (min-width: 600px) {
  #account { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 900px) {
  #account { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 1200px) {
  #account { grid-template-columns: repeat(4, 1fr); }
}
</style>

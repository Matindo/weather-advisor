<template>
  <div id="register-form">
    <b-form @submit.prevent="submit()" @reset="reset()" v-show="show">
      <b-form-row class="sect" title="Personal Info">
        <b-col cols="12" lg="6">
          <b-form-group id="first-name" label="First Name:" label-for="input-first-name" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-first-name" v-model="formData.fname" placeholder="e.g Alex" required trim></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="last-name" label="Other Name:" label-for="input-last-name" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-last-name" v-model="formData.lname" placeholder="e.g Baker" required trim></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="pword" label="Password:" label-for="input-pword" label-cols-lg="4" content-cols-lg  :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-pword" v-model="formData.pass" type="password" required></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="confirm-pword" label="Confirm Password:" label-for="input-conpass" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-conpass" v-model="formData.passConfirmed" type="password" required></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="sub-email" label="Email:" label-for="input-sub-email" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-sub-email" v-model="formData.email" type="email" required trim  :disabled="getEmail === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12">
          <b-form-group label="Is your phone number the same as your Telegram number? ">
            <b-form-radio-group id="rg-telegram" v-model="sameTelegram" :options="teleOptions" name="rg-telegram"></b-form-radio-group>
          </b-form-group>
        </b-col>
        <b-col cols="12" v-show="!sameTelegram">
          <b-form-group id="telegram" label="Telegram No:" label-for="input-telegram" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-telegram" v-model="formData.telegram" type="telephone" required trim :disabled="getGram === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <div class="w-100 decider py-2">
          <b-form-checkbox id="check-gram" v-model="formData.getGram" value="yes" unchecked-value="no"> Get Telegram Notifications</b-form-checkbox>
        </div>
      </b-form-row>
      <b-form-row class="location" title="Your Location">
        <h3 class="w-100">Your Weather location</h3>
        <!--b-button class="mt-3" pill variant="outline-light" block @click="copyLocation()" v-show="city !== '' || location.length != 0">
          Use default location as your preferred weather location
        </b-button-->
        <b-button class="mt-2 mb-1" pill variant="outline-warning" block @click="setLocation()">
          Set current location as your preferred weather location
        </b-button>
        <div class="search my-3">
          ...or type in your preferred city:
          <b-input type="text" placeholder="e.g. Thika" v-model="formData.location" />
        </div>
      </b-form-row>
      <div class="form-footer">
        <b-button type="submit" size="lg" variant="primary">Submit Details</b-button>
        <b-button type="reset" size="lg" variant="warning">Reset Form</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import { locationMixin } from '@/mixins/locationMixin'
import * as menuOptions from '@/helpers/menuOptons'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'RegisterForm',
  mixins: [locationMixin],
  props: {
    presets: {
      type: Object,
      required: true
    }
  },
  computed: {
    ...mapGetters({
      city: 'CITY',
      location: 'LOCATION'
    })
  },
  data: function () {
    return {
      show: true,
      sameTelegram: true,
      currentPage: 0,
      searchQuery: '',
      weatherOptions: menuOptions.weatherDataOptions,
      formData: {
        fname: '', lname: '', passConfirmed: '', pass: '', email: '', getGram: 'no', phone: '', location: ''
      }
    }
  },
  methods: {
    submit: function () {
      const formData = new FormData()
      formData.append('fname', this.formData.fname)
      formData.append('lname', this.formData.lname)
      formData.append('pword', this.formData.passConfirmed)
      formData.append('email', this.formData.email)
      formData.append('phone', this.formData.phone)
      formData.append('getTelegram', this.formData.getGram)
      formData.append('location', this.formData.location)
      axios({
        method: 'POST',
        url: `./api/Subscribe.php?action=add${this.presets.userType}`,
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
      })
    },
    reset: function () {
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    copyLocation: function () {
      if (localStorage.getItem('defaultLocation')) {
        this.formData.location = JSON.stringify({ lon: this.location[0], lat: this.location[1] })
      } else if (localStorage.getItem('defaultCity')) {
        this.formData.location = this.city
      } else {
        this.$store.dispatch('SET_STATUS', 'dark')
        this.$store.dispatch('SET_MESSAGE', 'No default city or location set')
        this.$root.$emit('showSnackbar')
      }
    },
    setLocation: function () {
      this.getLocation()
      setInterval(() => {
        this.formData.location = JSON.stringify({ lon: this.longitude, lat: this.lattitude })
      }, 1000)
      this.$store.dispatch('SET_STATUS', 'info')
      this.$store.dispatch('SET_MESSAGE', 'Current location set!')
      this.$root.$emit('showSnackbar')
    }
  }
}
</script>

<style lang="scss" scoped>
#register-form {
  font-family: RaleWay;
  background: #222;
  color: var(--white);
  padding: .5rem;
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, 0.537), rgba(5, 5, 5, .58), rgba(5, 5, 5, 1)),url('../assets/images/brian-tromp-VTYDkU-n3_s-unsplash.jpg');
  background-position: center;
  background-size: cover;
}
.form-row {
  display: flex;
  flex-direction: row;
  justify-content: left;
  align-items: center;
  width: 100%;
  flex-wrap: wrap;
  padding: .25rem;
  margin: .1rem;
  &.location {
    flex-direction: column;
    justify-content: center;
  }
}
.form-group, .decider {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  flex-wrap: wrap;
  width: 90%;
}
.form-control {
  margin-left: 5px;
}
.form-footer {
  display: flex;
  width: 100%;
  justify-content: space-around;
  align-items: center;
  padding: 1rem 3rem;
  border-top: 3px groove #f3f9fa;
}
</style>

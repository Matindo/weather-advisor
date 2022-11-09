<template>
  <div id="register-form">
    <b-form @submit.prevent="submit()" @reset="reset()" v-show="show">
      <b-form-row class="sect" title="Personal Info">
        <h3 class="w-100">Your Personal Details</h3>
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
        <h3 class="w-100">Contact Details</h3>
        <div class="w-100 decider py-2">
          <b-form-checkbox id="check-email" v-model="getEmail" value="yes" unchecked-value="no"> E-mail</b-form-checkbox>
          <b-form-checkbox id="check-gram" v-model="getGram" value="yes" unchecked-value="no"> Telegram</b-form-checkbox>
          <b-form-checkbox id="check-WA" v-model="getWA" value="yes" unchecked-value="no"> WhatsApp</b-form-checkbox>
          <b-form-checkbox id="check-text" v-model="getText" value="yes" unchecked-value="no"> SMS</b-form-checkbox>
        </div>
        <b-col cols="12" lg="6">
          <b-form-group id="telegram" label="Telegram No:" label-for="input-telegram" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-telegram" v-model="formData.telegram" type="telephone" required trim :disabled="getGram === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="whatsapp" label="WhatsApp No:" label-for="input-whatsapp" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-whatsapp" v-model="formData.whatsapp" type="telephone" required trim :disabled="getWA === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="sub-email" label="Email:" label-for="input-sub-email" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-sub-email" v-model="formData.email" type="email" required trim  :disabled="getEmail === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="sub-phone" label="Telephone:" label-for="input-sub-phone" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-sub-phone" v-model="formData.phone" type="telephone" required trim  :disabled="getText === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row class="location" title="Your Location">
        <h3 class="w-100">Your Weather location</h3>
        <b-button class="mt-3" pill variant="outline-light" block @click="copyLocation">
          Use default location as your preferred weather location
        </b-button>
        <b-button class="mt-3" pill variant="outline-warning" block @click="setLocation">
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
  data: function () {
    return {
      show: true,
      currentPage: 0,
      searchQuery: '',
      weatherOptions: menuOptions.weatherDataOptions,
      getEmail: 'no',
      getGram: 'no',
      getText: 'no',
      getWA: 'no',
      formData: {
        fname: '', lname: '', passConfirmed: '', pass: '', email: '', telegram: '', whatsapp: '', phone: '', location: ''
      }
    }
  },
  methods: {
    submit: function () {
      const formData = new FormData()
      formData.append('fname', formData.fname)
      formData.append('lname', formData.lname)
      formData.append('pword', formData.passConfirmed)
      formData.append('email', formData.email)
      formData.append('phone', formData.phone)
      formData.append('telegram', formData.telegram)
      formData.append('whatsapp', formData.whatsapp)
      formData.append('location', formData.location)
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
        this.formData.location = localStorage.getItem('defaultLocation')
      } else {
        this.$store.dispatch('SET_STATUS', 'dark')
        this.$store.dispatch('SET_MESSAGE', 'No default city or location set')
        this.$root.$emit('showSnackbar')
      }
    },
    setLocation: function () {
      this.formData.location = JSON.stringify(this.getLocation())
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
  background-image: linear-gradient(to bottom, rgba(34, 34, 34, .15), rgba(5, 5, 5, .88), rgba(5, 5, 5, 1)),url('../assets/images/brian-tromp-VTYDkU-n3_s-unsplash.jpg');
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

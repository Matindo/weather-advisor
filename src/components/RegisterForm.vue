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
          <b-form-group id="email" label="Email:" label-for="input-email" label-cols-lg="4" content-cols-lg  :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-email" v-model="formData.email" type="email" required trim></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="phone" label="Telephone:" label-for="input-phone" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-phone" v-model="formData.phone" type="telephone" required trim></b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row class="sect" title="Contact Info">
        <h3 class="w-100">How Do You Want To Receive Information?</h3>
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
            <b-form-input id="input-sub-email" v-model="formData.subEmail" type="email" required trim  :disabled="getEmail === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
        <b-col cols="12" lg="6">
          <b-form-group id="sub-phone" label="Telephone:" label-for="input-sub-phone" label-cols-lg="4" content-cols-lg :invalid-feedback="invalidNameFeedback">
            <b-form-input id="input-sub-phone" v-model="formData.subPhone" type="telephone" required trim  :disabled="getText === 'no'"></b-form-input>
          </b-form-group>
        </b-col>
      </b-form-row>
      <b-form-row class="sect" title="Information required">
        <h3 class="w-100">What Information Do You Need?</h3>
        <b-form-group label="Select from these options:" v-slot="{ ariaDescribedby }">
          <b-form-checkbox-group id="check-weather" v-model="formData.selectedWeather" :options="weatherOptions" :aria-describedby="ariaDescribedby" name="weather-options"
          ></b-form-checkbox-group>
        </b-form-group>
      </b-form-row>
    </b-form>
  </div>
</template>

<script>
import * as menuOptions from '@/helpers/menuOptons'

export default {
  name: 'RegisterForm',
  props: {
    presets: {
      type: Object,
      required: true
    }
  },
  data: function () {
    return {
      show: true,
      weatherOptions: menuOptions.weatherDataOptions,
      getEmail: 'no',
      getGram: 'no',
      getText: 'no',
      getWA: 'no',
      formData: {
        fname: '', lname: '', email: '', phone: '', subEmail: '', telegram: '', whatsapp: '', subPhone: '', selectedWeather: []
      }
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
.form-row {
  display: flex;
  flex-direction: row;
  justify-content: left;
  align-items: center;
  width: 100%;
  flex-wrap: wrap;
}
.sect {
  padding: .25rem;
  margin: .1rem;
  border-bottom: 1px ridge rgb(175, 174, 174);
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
</style>

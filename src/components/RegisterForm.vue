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
      <div style="overflow:auto;">
        <div style="float:right;">
          <b-button variant="outline-light" id="prevBtn" class="m-1" @click="navigate(-1)">Previous</b-button>
          <b-button variant="outline-light" id="nextBtn" class="m-1" @click="navigate(1)">Next</b-button>
        </div>
      </div>
      <div style="text-align:center;margin-top:40px;">
        <span class="step"></span>
        <span class="step"></span>
        <span class="step"></span>
      </div>
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
      currentPage: 0,
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
    },
    showPage: function (pageNumber) {
      const x = document.getElementsByClassName('sect')
      x[pageNumber].style.display = 'flex'
      // updste the Previous/Next buttons
      if (pageNumber === 0) {
        document.getElementById('prevBtn').style.display = 'none'
      } else {
        document.getElementById('prevBtn').style.display = 'inline'
      }
      if (pageNumber === (x.length - 1)) {
        document.getElementById('nextBtn').innerHTML = 'Submit'
      } else {
        document.getElementById('nextBtn').innerHTML = 'Next'
      }
      // Displays the correct step indicator:
      this.fixStepIndicator(pageNumber)
    },
    navigate: function (n) {
      // Figure out which page to display
      const x = document.getElementsByClassName('sect')
      // Exit the function if any field in the current tab is invalid:
      if (n === 1 && !this.validateForm()) {
        return false
      }
      // Hide the current tab:
      x[this.currentPage].style.display = 'none'
      // Increase or decrease the current tab by 1:
      this.currentPage = this.currentPage + n
      // if you have reached the end of the form... :
      if (this.currentPage >= x.length) {
        // ...the form gets submitted:
        this.submit()
        return false
      }
      // Otherwise, display the correct tab:
      this.showPage(this.currentPage)
    },
    fixStepIndicator: function (pageNumber) {
      // This function removes the "active" class of all steps...
      let i; const x = document.getElementsByClassName('step')
      for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(' active', '')
      }
      // ... and adds the "active" class to the current step:
      x[pageNumber].className += ' active'
    },
    validateForm: function () {
      // This function deals with validation of the form fields
      let i; let valid = true
      const x = document.getElementsByClassName('sect')
      const y = x[this.currentPage].getElementsByTagName('input')
      // A loop that checks every input field in the current tab:
      for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value === '') {
          // add an "invalid" class to the field:
          y[i].className += ' invalid'
          // and set the current valid status to false:
          valid = false
        }
      }
      // If the valid status is true, mark the step as finished and valid:
      if (valid) {
        document.getElementsByClassName('step')[this.currentPage].className += ' finish'
      }
      return valid // return the valid status}
    }
  },
  mounted: function () {
    this.showPage(this.currentPage)
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
}
.sect {
  padding: .25rem;
  margin: .1rem;
  // border-bottom: 1px ridge rgb(175, 174, 174);
  display: none;
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
.step {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbbbbb;
  border: none;
  border-radius: 50%;
  display: inline-block;
  opacity: 0.5;
}
.step.active {
  opacity: 1;
}
.step.finish {
  background-color: #04AA6D;
}
</style>

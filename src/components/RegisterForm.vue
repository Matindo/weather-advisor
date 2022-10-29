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
      <b-form-row class="sect" title="Information required">
        <h3 class="w-100">What Information Do You Need?</h3>
        <div class="weather-info">
          <div v-for="(option, index) in weatherOptions" :key="index">
            <label class="option-container">{{option.text}}
              <input type="checkbox" v-model="formData.selectedWeather" :value="option.value">
              <span class="checkmark"></span>
            </label>
          </div>
          <p>Selected options: {{formData.selectedWeather}}</p>
        </div>
        <h3 class="w-100">Notification Regularity</h3>

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
        fname: '', lname: '', passConfirmed: '', pass: '', email: '', telegram: '', whatsapp: '', phone: '', selectedWeather: []
      }
    }
  },
  methods: {
    submit: function () {
      // gather data and send to server
    },
    reset: function () {
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
      x[this.currentPage].style.display = 'none' // hide current page
      this.currentPage = this.currentPage + n // next/previous page
      if (this.currentPage >= x.length) { // last page
        this.submit() // submit form
        return false
      }
      this.showPage(this.currentPage) // display new page
    },
    fixStepIndicator: function (pageNumber) {
      let i; const x = document.getElementsByClassName('step')
      for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(' active', '') // no active indicator
      }
      x[pageNumber].className += ' active' // set active indicator
    },
    validateForm: function () {
      return true
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
.weather-info {
  display: grid;
  grid: auto-flow dense 38px / repeat(4, minmax(100px, 1fr));
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
.option-container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.option-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

/* On mouse-over, add a grey background color */
.option-container:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the checkbox is checked, add a blue background */
.option-container input:checked ~ .checkmark {
  background-color: #2196F3;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.option-container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.option-container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style>

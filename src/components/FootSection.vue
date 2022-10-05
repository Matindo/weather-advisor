<template>
  <div id="foot-section">
    <b-row id="footer" class="p-3 mx-2" align-h="even" align-v="stretch">
      <b-col id="main">
        <span class="logo"><img src='../assets/images/logo.png' class="logo-img" /><h1>Misimu</h1></span>
        <b-button variant="outline-warning" class="w-100 my-2" block @click="$bvModal.show('modal-subscribe')">Get Weather Alerts</b-button>
      </b-col>
      <b-col id="links">
        <h2>Navigate </h2>
        <h5 class="my-2"><router-link to="/" >Home</router-link></h5>
        <h5 class="my-2"><router-link to="/forecasts">Weather & Forecasts</router-link></h5>
      </b-col>
      <b-col id="functions">
        <h2>Your Weather </h2>
        <b-input-group size="sm" class="my-2">
          <b-input-group-prepend is-text>
            <!--b-button variant="outline-light" @click="searchWeather()"--><b-icon icon="search"></b-icon><!--/b-button-->
          </b-input-group-prepend>
          <b-form-input type="search" placeholder="Search any city's weather" v-model="city" @keypress.enter="search()"></b-form-input>
        </b-input-group>
        <p class="text-center w-100 my-1">- or -</p>
        <b-button class="weather-getter w-100" size="sm" variant="outline-light" pill @click="locationWeather()">Get Current Location's Weather</b-button>
      </b-col>
    </b-row>
    <hr />
    <b-row class="copyright w-100 my-2" align-h="centerr">
      <b-col>
        <p class="w-100" style="text-align: center;">&copy; Misimu {{ new Date().getFullYear() }}</p></b-col>
    </b-row>
  </div>
</template>

<script>
import { locationMixin } from '@/mixins/locationMixin'

export default {
  name: 'FootSection',
  mixins: [locationMixin],
  data: function () { return { city: '' } },
  methods: {
    locationWeather: function () {
      this.getLocation()
      this.$store.dispatch('SET_LOCATION', [this.longitude, this.lattitude]).then(() => this.$router.push('/forecasts'))
    },
    search: function () {
      this.$store.dispatch('SET_CITY', this.city).then(() => this.$router.push('/forecasts'))
    }
  }
}
</script>

<style lang="scss" scoped>
#foot-section {
  background-color: #222;
  // background: linear-gradient(to bottom, var(--BGcolor), rgba(13, 13, 14, 0.8));
  padding: 5px 20px;
  transition: 0.14s all ease-out;
  color: var(--white);
  bottom: 0;
}
#main, #links, #functions {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  a {
    text-decoration: none;
    color: var(--white);
    &:hover {
      text-decoration: underline;
    }
  }
  h1 {
    width: 100%;
    font-weight: 900;
    text-align: center;
  }
}
</style>

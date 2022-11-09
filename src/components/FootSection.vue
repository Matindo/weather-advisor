<template>
  <div id="foot-section">
    <div id="brand">
      <span class="logo"><img src='../assets/images/logo.png' class="logo-img" /><h1 class="mb-0">Misimu</h1></span>
      <span><h5 class="my-0">Your One-Stop weather App</h5></span>
    </div>
    <div id="footer-content">
      <h3 class="weather">Get Your Weather</h3>
      <b-input-group size="sm" class="my-2 search">
        <b-input-group-append is-text @click="searchWeather()">
          <b-icon icon="search"></b-icon>
        </b-input-group-append>
        <b-form-input type="search" placeholder="Search any city's weather" v-model="city" @keypress.enter="search()"></b-form-input>
      </b-input-group>
      <b-button class="weather-getter my-0" variant="outline-light" pill @click="locationWeather()">Get Current Location's Weather</b-button>
      <div class="subscribe">
        <h3>Get Notified</h3>
        <b-button variant="outline-warning" class="w-75 my-2 mx-auto" block @click="subscribe()">Subscribe & Get Alerts</b-button>
      </div>
      <div class="socials">
        <ul class="social-links">
          <li class="social-link"><a id="discord" href="#"><b-icon font-scale="2" icon="discord"></b-icon></a></li>
          <li class="social-link"><a id="twitter" href="#"><b-icon font-scale="2" icon="twitter"></b-icon></a></li>
          <li class="social-link"><a id="github" href="#"><b-icon font-scale="2" icon="github"></b-icon></a></li>
          <li class="social-link"><a id="whatsapp" href="#"><b-icon font-scale="2" icon="whatsapp"></b-icon></a></li>
          <li class="social-link"><a id="telegram" href="#"><b-icon font-scale="2" icon="telegram"></b-icon></a></li>
        </ul>
      </div>
    </div>
    <div id="copyright">
      <p class="w-100" style="text-align: center;">&copy; Misimu {{ new Date().getFullYear() }}</p>
    </div>
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
      this.$store.dispatch('SET_LOCATION', [this.longitude, this.lattitude]).then(() => this.$router.push('/'))
    },
    search: function () {
      this.$store.dispatch('SET_CITY', this.city).then(() => this.$router.push('/'))
    },
    subscribe: function () {
      this.$root.$emit('footerSubscribe')
    }
  }
}
</script>

<style lang="scss" scoped>
#foot-section {
  background-color: var(--navigator-bg);
  display: grid;
  grid-template-columns: min-max(300px, 1fr) min-max(300px, 2fr) ;
  grid-template-rows: auto min-content;
  grid-auto-flow: row;
  column-gap: 2rem;
  row-gap: .8rem;
  padding: 5px 3rem;
  transition: 0.14s all ease-out;
  color: var(--white);
  margin-bottom: 0;
  align-items: flex-start;
  justify-content: center;
}
#brand {
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
#brand {
  grid-area: 1 / 1 / 2 / 2;
}
#footer-content {
  grid-area: 1 / 2 / 2 / 3;
  display: grid;
  grid-template-rows: min-content min-content min-content min-content;
  grid-template-columns: 1fr 1fr;
  align-items: flex-start;
  justify-content: center;
  padding: 1rem;
}
.weather {
  grid-area: 1 / 1 / 2 / end;
  width: 100%;
  text-align: center;
}
.search {
  grid-area: 2 / 1 / 3 / 2;
}
.weather-getter {
  grid-area: 2 / 2 / 3 / 3;
  margin-left: 1rem;
}
.subscribe {
  grid-area: 3 / 1 / 4 / end;
  padding-top: 1.2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  width: 100%;
}
.weather, .subscribe {
  h3 {
    font-weight: normal;
  }
}
.socials {
  grid-area: 4 / 1 / end / end;
  width: 100%;
  display: flex;
  justify-content: space-around;
  margin-top: 1rem;
}
.social-links {
  list-style: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  width: 100%;
  li {
    display: block;
    width: auto;
    margin: 8px;
    a {
      color: var(--white);
      transition: all .2s ease-in;
      border-radius: 50%;
      &::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        transform: scale(.9);
        z-index: -1;
      }
      &#telegram::before{
        background: rgb(11, 11, 126);
      }
      &#twitter::before{
        background: rgb(79, 39, 255);
      }
      &#whatsapp::before{
        background: rgb(10, 184, 10);
      }
      &#discord::before{
        background: rgb(137, 18, 184);
      }
      &#github::before{
        background: rgb(151, 2, 2);
      }
    }
    a:hover::before{
      transform: scale(1.0);
    }
    a#telegram:hover {
      text-shadow: 0 0 5px rgb(11, 11, 126);
      box-shadow: 0 0 5px rgb(11, 11, 126);
      color: rgb(11, 11, 126);
    }
    a#twitter:hover {
      box-shadow: 0 0 5px rgb(79, 39, 255);
      text-shadow: 0 0 5px rgb(79, 39, 255);
      color: rgb(79, 39, 255);
      &::before{
        box-shadow: 0 0 15px rgb(79, 39, 255);
      }
    }
    a#whatsapp:hover {
      text-shadow: 0 0 5px rgb(10, 184, 10);
      box-shadow: 0 0 5px rgb(10, 184, 10);
      color: rgb(10, 184, 10);
      &::before{
        box-shadow: 0 0 15px rgb(10, 184, 10);
      }
    }
    a#discord:hover {
      box-shadow: 0 0 5px rgb(137, 18, 184);
      text-shadow: 0 0 5px rgb(137, 18, 184);
      color: rgb(137, 18, 184);
      &::before{
        box-shadow: 0 0 15px rgb(137, 18, 184);
      }
    }
    a#github:hover {
      box-shadow: 0 0 15px rgb(151, 2, 2);
      text-shadow: 0 0 15px rgb(151, 2, 2);
      color: rgb(151, 2, 2);
      &::before{
        box-shadow: 0 0 15px rgb(151, 2, 2);
      }
    }
  }
}
#copyright {
  grid-area: 2 / 1 / 3 / 3;
  width: 100%;
  border-top: 1px solid var(--white);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
}
</style>

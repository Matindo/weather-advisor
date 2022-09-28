<template>
  <b-container id="home" fluid>
    <div class="jumbotron">
      <div class="slide-container">
        <div v-for="(slide, index) in slides" :key="index"></div>
      </div>
      <div id="scroll-down">
        <b-icon icon="arrow-down-short" animation="fade" font-scale="4" style="width: 4rem; height: 4rem;"></b-icon>
      </div>
    </div>
    <b-row id="forecast" class="my-2 p-2">
      <div class="w-100">
        <h1>Forecasts</h1>
      </div>
      <div class="content">
        <b-col cols="12" md="6" class="right">
          <p>Recieve the weather data for your area or region from an aaccurate source. Alse recieve weather forecasts for upto 8 days to prepare yourself for any events and activities that may be affected.</p>
          <span class="more-button" @click="$router.push('/forecasts')">
            <b-icon icon="arrow-right-circle" style="width: 30px; height: 30px;"></b-icon>
          </span>
        </b-col>
      </div>
    </b-row>
    <b-row id="ngos">
      <div class="w-100">
        <h1 class="right">Relief Organizations</h1>
      </div>
      <div class="content">
        <b-col cols="12" md="6">
          <p>Are you a relief organization that works in areas affected by adverse weather phenomena? We have alerts and advisories here for you to help you prepare and allocate your limited resources accordingly.</p>
          <span class="more-button" @click="$router.push('/ngos')">
            <b-icon icon="arrow-right-circle" style="width: 30px; height: 30px;"></b-icon>
          </span>
        </b-col>
      </div>
    </b-row>
    <b-row id="accounts">
      <div class="w-100">
        <h1>Register</h1>
      </div>
      <div class="content" >
        <b-col cols="12" md="6" class="right">
          <p>Are you a professional, student or citizen who would simply like to get weather notifications and predictions customized for your needs? Register with us and choose your mode of receiving weather alerts!</p>
          <span class="more-button" @click="$router.push('/accounts')">
            <b-icon icon="arrow-right-circle" style="width: 30px; height: 30px;"></b-icon>
          </span>
        </b-col>
      </div>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'HomeView',
  data: function () {
    return {
      slides: []
    }
  },
  computed: {
    daytime: function () {
      var currentHour = new Date().getHours()
      var timeOfDay = ''
      console.log(currentHour)
      if (currentHour > 19 || currentHour < 6) {
        timeOfDay = 'night'
      } else if (currentHour > 6 && currentHour < 9) {
        timeOfDay = 'morning'
      } else if (currentHour > 9 && currentHour < 12) {
        timeOfDay = 'mid-morning'
      } else if (currentHour > 12 && currentHour < 15) {
        timeOfDay = 'noon'
      } else if (currentHour > 15 && currentHour < 19) {
        timeOfDay = 'evening'
      }
      console.log(timeOfDay)
      return timeOfDay
    }
  },
  mounted: function () {
    document.getElementById('home').style.backgroundImage = `linear-gradient(to bottom, rgba(34, 34, 34, .95), rgba(5, 5, 5, .5)),url('https://source.unsplash.com/1600x900/?${this.daytime}')`
  }
}
</script>

<style lang="scss" scoped>
* {
  font-size: 1.5rem;
}
#home {
  margin-top: 0;
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
}
h1 {
  color: var(--white);
  font-size: 36px;
}

.jumbotron {
  height: 70vh;
  width: 100%;
  background-color: rgba(39, 101, 101, 0.1);
  margin: o 0 3rem 0;
  border-radius: 1.3rem;
  #scroll-down {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80px;
    height: 80px;
    top: 73%;
    left: calc(50% - 2rem);
    border-radius: 50%;
    background: var(--primary);
    transition: all ease 400ms;
    &:hover{
      background: #ab470a;
    }
  }
}

.row {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: .5rem 6rem;
}

.right {
  float: right;
  justify-content: right;
}

.more-button {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 5px;
  padding: 8px;
  border-radius: 1rem;
  color: var(--primary);
  font-size: 2rem;
  transition: all ease 350ms;
  &:hover {
    color: var(--success);
    background: rgba(34, 34, 34, 0.048);
  }
}
</style>

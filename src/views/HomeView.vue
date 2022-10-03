<template>
  <b-container id="home" fluid>
    <b-jumbotron header="Welcome to your one-stop weather advisory web application, where we provide you with current weather information, weather forecasts and even weather alerts customized just for you, from any location, any time!" container-fluid="sm">
    </b-jumbotron>
    <b-row id="forecast" class="my-5 p-2">
      <div class="w-100">
        <h1>Forecasts</h1>
      </div>
      <div class="content">
        <b-col cols="12" md="6" class="right">
          <p>Recieve the weather data for your area or region from an aaccurate source. Alse recieve weather forecasts for upto 8 days to prepare yourself for any events and activities that may be affected.</p>
          <span class="more-button">
            <b-button pill variant="outline-light" @click="$router.push('/forecasts')">
              Go To Forecasts <b-icon icon="arrow-right-circle" style="width: 30px; height: 30px;"></b-icon>
            </b-button>
          </span>
        </b-col>
      </div>
    </b-row>
    <b-row id="ngos" class="my-4 p-2">
      <div class="w-100">
        <h1 class="right">Relief Organizations</h1>
      </div>
      <div class="content">
        <b-col cols="12" md="6">
          <p>Are you a relief organization that works in areas affected by adverse weather phenomena? We have alerts and advisories here for you to help you prepare and allocate your limited resources accordingly.</p>
          <span class="more-button">
            <b-button pill block variant="outline-warning" @click="$bvModal.show('modal-subscribe')">Request Information</b-button>
          </span>
        </b-col>
      </div>
    </b-row>
    <b-row id="accounts" class="mt-3 mb-2 p-2">
      <div class="w-100">
        <h1>Subscribe</h1>
      </div>
      <div class="content" >
        <b-col cols="12" md="6" class="right">
          <p>Are you a professional, student or citizen who would simply like to get weather notifications and predictions customized for your needs? Register with us and choose your mode of receiving weather alerts!</p>
          <span class="more-button">
            <b-button pill block variant="outline-success" @click="$bvModal.show('modal-subscribe')">Click to Subscribe</b-button>
          </span>
        </b-col>
      </div>
    </b-row>
    <b-modal id="modal-subscribe" size="xl" centered hide-footer hide-header>
      <register-form :presets="formOptions" />
    </b-modal>
  </b-container>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue'
export default {
  components: { RegisterForm },
  name: 'HomeView',
  data: function () {
    return {
      formOptions: { ngo: false, farmer: false }
    }
  },
  computed: {
    daytime: function () {
      var currentHour = new Date().getHours()
      var timeOfDay = ''
      console.log(currentHour)
      if (currentHour >= 19 || currentHour < 6) {
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
  methods: {
    scrolldown: function () {
      const first = document.getElementById('forecast')
      first.scrollIntoView({ behaviour: 'smooth', block: 'atart', inline: 'center' })
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
  margin-bottom: 0;
  padding-bottom: 2rem;
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
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-align: center;
  font-family: Georgia, 'Times New Roman', Times, serif;
  margin: 0 1rem 3rem 1rem;
  padding-top: 3rem;
}
.row {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-right: 6rem;
  margin-left: 6rem;
  border-radius: 1rem;
}

#forecast {
  background-image: linear-gradient(to right, rgba(34, 34, 34, .15), rgba(5, 5, 5, .88), rgba(5, 5, 5, 1)),url('../assets/images/hendrik-kespohl-UPnxtRNH8q8-unsplash.jpg');
  background-position: top center;
  background-size: cover;
}

#ngos {
  background-image: linear-gradient(to left, rgba(34, 34, 34, .15) 0%, rgba(5, 5, 5, .9) 60%, rgba(5, 5, 5, 1) 100%),url('../assets/images/swapnil-dwivedi-Bwbq9_AuZ7c-unsplash.jpg');
  background-position: top left;
  background-size: cover;
}

#accounts {
  background-image: linear-gradient(to right, rgba(34, 34, 34, .15) 0%, rgba(5, 5, 5, .88) 60%, rgba(5, 5, 5, 1) 100%),url('../assets/images/brett-jordan-LPZy4da9aRo-unsplash.jpg');
  background-position: center left;
  background-size: cover;
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
}

@media all and (max-width: 540px) {
  .row {
    margin-left: 1rem;
    margin-right: 1rem;
  }
}
</style>

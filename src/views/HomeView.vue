<template>
  <b-container id="home" fluid>
    <div class="jumbotron">
      <div class="slide-container">
        <div v-for="(slide, index) in slides" :key="index"></div>
      </div>
      <div id="scroll-down">
        <b-icon icon="arrow-down-short" animation="fade" font-scale="4" style="width: 60px; height: 60px;"></b-icon>
      </div>
    </div>
    <b-row id="forecast">
      <h2>Forecasts</h2>
    </b-row>
    <b-row id="ngos">
      <h2>Relief Organizations</h2>
    </b-row>
    <b-row id="accounts">
      <h2>Sign Up</h2>
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
  }
}
</script>

<style lang="scss" scoped>
h1 {
  color: var(--white)
}

.jumbotron {
  height: 70vh;
  width: 100%;
  background-color: rgba(39, 101, 101, 0.1);
  margin: 1rem 0 3rem 0;
  border-radius: 1.3rem;
  #scroll-down {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80px;
    height: 80px;
    top: 80%;
    left: 50%;
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
  min-height: 300px;
  margin: 1rem 3rem;
}
</style>

<template>
  <b-navbar toggleable="lg" type="dark" class="navbar">
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="middle-nav">
        <b-nav-item to="/" exact exact-active-class="active">HOME</b-nav-item>
        <b-nav-item to="/forecasts" exact exact-active-class="active">WEATHER & FORECASTS</b-nav-item>
        <!--b-nav-item to="/ngos" exact exact-active-class="active">RELIEF ORGANIZATIONS</b-nav-item>
        <b-nav-item to="/accounts" exact exact-active-class="active">REGISTER</b-nav-item-->
      </b-navbar-nav>

      <!-- Right aligned nav items>
      <b-navbar-nav class="ml-auto mr-2">
        <!b-nav-item to="/about" exact exact-active-class="active" v-show="user !== null">MY PAGE</b-nav-item>
        <b-nav-item-dropdown right  v-if="profile.name !== '' && user.name !== null">
          <! Using 'button-content' slot>
          <template #button-content>
            <em>{{profile.name}}</em>
          </template>
          <b-dropdown-item to="/profile" v-show="user !== null">My Profile</b-dropdown-item>
          <b-dropdown-item @click="logout()" v-show="user !== null">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item @click="login()" v-else>Sign In</b-nav-item>
      </b-navbar-nav-->
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters({
      user: 'USER'
    }),
    profile: function () {
      if (this.user === null) {
        return { name: '', dpic: '' }
      } else {
        return { name: this.user.userName, dpic: this.user.picture }
      }
    }
  },
  data: function () {
    return {
    }
  },
  methods: {
    logout: function () {
      // log user out and route to home page
      this.$store.dispatch('LOG_OUT').then(() => {
        this.$router.push('/')
      })
    },
    login: function () {
      this.$router.push('/account')
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  background-color: var(--navigator-bg);
  // background: linear-gradient(to bottom, var(--BGcolor), rgba(13, 13, 14, 0.8));
  padding: 5px 20px;
  transition: 0.14s all ease-out;
  color: rgb(198, 200, 202);
  margin-bottom: 0;
}
.navbar-brand {
  font-family: 'Lobster', cursive;
  font-size: xx-large;
  color: var(--white)
}
.middle-nav {
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-left: auto;
}
.nav-item::after {
  content: '';
  position: relative;
  display: block;
  height: .2rem;
  width: 0%;
  background-color: antiquewhite;
}
.nav-item:hover{
  transition: ease-in-out all .4s;
  -moz-transition: ease-in-out all .4s;
  -webkit-transition: ease-in-out all .4s;
  color:antiquewhite;
  text-decoration:none;
}
.nav-item:hover::after{
  transition: ease-in-out all .4s;
  -moz-transition: ease-in-out all .4s;
  -webkit-transition: ease-in-out all .4s;
  height: .2rem;
  width: 100%;
}
.nav-item a.active{
  color: var(--brilliant-white);
}
.nav-item:has(a.active)::after{
  height: .2rem;
  width: 100%;
  background-color: var(--brilliant-white);
}
.navbar button.navbar-toggler {
  color: var(--white);
}
.nav-item {
  display: block;
  width: 100%;
  border-right: 1px solid #999;
  text-align: center;
  &:last-child {
    border-right: none;
  }
}
</style>

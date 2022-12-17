<template>
  <b-navbar type="dark" id="navbar">
    <b-navbar-brand to="/" class="brand">
      <img src="../assets/images/logo.png" height="48" width="48" alt="logo" />
      <span class="title">Misimu</span>
    </b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item-dropdown dropright no-caret>
        <template #button-content>
          <div class="button-cnt"><b-icon font-scale="2" icon="check2-circle"></b-icon>Subscriptions</div>
        </template>
        <b-dropdown-item @click="subscribe" v-show="!isSubscribed">Subscribe</b-dropdown-item>
        <b-dropdown-item @click="tryLogin" v-show="!isLoggedIn && isSubscribed">Sign In</b-dropdown-item>
        <b-dropdown-item @click="$router.push('/profile')" v-show="isLoggedIn && isSubscribed">My Subscriptions</b-dropdown-item>
        <b-dropdown-item @click="logout" v-show="isLoggedIn">Sign Out</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
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
    isSubscribed: function () {
      return this.user.subscriptions !== null
    },
    isLoggedIn: function () {
      return this.user.active
    }
  },
  methods: {
    logout: function () {
      // log user out and route to home page
      this.$store.dispatch('LOG_OUT').then(() => {
        this.$router.push('/')
      })
    },
    subscribe: function () {
      this.$root.$emit('headerSubscribe')
    },
    tryLogin: function () {
      this.$root.$emit('headerLogin')
    }
  }
}
</script>

<style lang="scss" scoped>
#navbar {
  transition: 0.14s all ease-out;
  color: rgb(198, 200, 202);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0;
  padding-inline: 2rem;
  padding-bottom: 0;
  background-color: rgba(19, 18, 18, 0);
}
.navbar-brand {
  font-family: 'Lobster', cursive;
  font-size: 2rem;
  color: var(--white);
  display: flex;
  justify-content: left;
  align-items: center;
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
  height: .2.8rem;
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
.button-cnt {
  display: flex;
  align-items: center;
}
</style>

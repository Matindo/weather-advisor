import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

const localDB = new VuexPersistence({
  supportCircular: true,
  storage: window.localStorage
})
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: { email: '', subscriptions: {}, active: false },
    city: '',
    location: [],
    userType: '',
    snackbarMessage: '',
    snackbarStatus: ''
  },
  getters: {
    USER: function (state) {
      return state.user
    },
    CITY: function (state) {
      return state.city
    },
    LOCATION: function (state) {
      return state.location
    },
    USER_TYPE: function (state) {
      return state.userType
    },
    MESSAGE: function (state) {
      return state.snackbarMessage
    },
    STATUS: function (state) {
      return state.snackbarStatus
    }
  },
  mutations: {
    READ_CITY: function (state) {
      if (localStorage.getItem('defaultCity')) {
        state.city = localStorage.getItem('defaultCity')
      }
    },
    READ_LOCATION: function (state) {
      if (localStorage.getItem('defaultLocation')) {
        const location = localStorage.getItem('defaultLocation')
        state.location = JSON.parse(location)
      }
    },
    SAVE_CITY: function (state, city) {
      if (localStorage.getItem('defaultCity') !== '') {
        localStorage.removeItem('defaultCity')
      }
      if (localStorage.getItem('defaultLocation') !== '') {
        localStorage.removeItem('defaultLocation')
        state.location.splice(0, state.location.length)
      }
      localStorage.setItem('defaultCity', city)
      state.city = city
    },
    SAVE_LOCATION: function (state, location) {
      if (localStorage.getItem('defaultLocation') !== '') {
        localStorage.removeItem('defaultLocation')
      }
      if (localStorage.getItem('defaultCity') !== '') {
        localStorage.removeItem('defaultCity')
        state.city = ''
      }
      localStorage.setItem('defaultLocation', JSON.stringify(location))
      state.location = location
    },
    SET_CITY: function (state, city) {
      state.location.splice(0, state.location.length)
      state.city = city
    },
    SET_LOCATION: function (state, location) {
      state.city = ''
      state.location = location
    },
    SET_USER_TYPE: function (state, type) {
      state.userType = type
    },
    SET_MESSAGE: function (state, message) {
      state.snackbarMessage = message
    },
    SET_STATUS: function (state, status) {
      state.snackbarStatus = status
    }
  },
  actions: {
    SET_DEFAULT_CITY: function (context, city) {
      context.commit('SAVE_CITY', city)
    },
    SET_DEFAULT_LOCATION: function (context, location) {
      context.commit('SAVE_LOCATION', location)
    },
    READ_DEFAULT_CITY: function (context) {
      context.commit('READ_CITY')
    },
    READ_DEFAULT_LOCATION: function (context) {
      context.commit('READ_LOCATION')
    },
    SET_CITY: function (context, city) {
      context.commit('SET_CITY', city)
    },
    SET_LOCATION: function (context, location) {
      context.commit('SET_LOCATION', location)
    },
    SET_USER_TYPE: function (context, payload) {
      context.commit('SET_USER_TYPE', payload)
    },
    SET_MESSAGE: function (context, payload) {
      context.commit('SET_MESSAGE', payload)
    },
    SET_STATUS: function (context, status) {
      context.commit('SET_STATUS', status)
    }
  },
  modules: {
  },
  plugins: [localDB.plugin]
})

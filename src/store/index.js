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
    user: {},
    city: '',
    location: []
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
    }
  },
  mutations: {
    READ_CITY: function (state) {
      if (localStorage.getItem('defaultCity')) {
        state.location = localStorage.getItem('defaultCity')
      }
    },
    READ_LOCATION: function (state) {
      if (localStorage.getItem('defaultLocation')) {
        state.location = localStorage.getItem('defaultLocation')
      }
    },
    SAVE_CITY: function (state, city) {
      if (localStorage.getItem('defaultCity') !== '') {
        localStorage.removeItem('defaultCity')
      }
      localStorage.setItem('defaultCity', city)
    },
    SAVE_LOCATION: function (state, location) {
      if (localStorage.getItem('defaultLocation') !== '') {
        localStorage.removeItem('defaultLocation')
      }
      localStorage.setItem('defaultLocation', location)
    }
  },
  actions: {
    SET_DEFAULT_CITY: function (context, city) {
      context.commit('SAVE_CITY', city)
    },
    SAVE_DEFAULT_LOCATION: function (context, location) {
      context.commit('SAVE_LOCATION')
    },
    READ_DEFAULT_CITY: function (context) {
      context.commit('READ_CITY')
    },
    READ_DEFAULT_LOCATION: function (context) {
      context.commit('READ_LOCATION')
    }
  },
  modules: {
  },
  plugins: [localDB.plugin]
})

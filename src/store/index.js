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
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
  plugins: [localDB.plugin]
})

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import {config} from '../config/config'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    isLoading: false,
    username: "",
    user_id: "",
    access_token: "",
    refresh_token: ""
  },
  mutations: {
    SET_LOADING: (state, loading) => {
      state.isLoading = loading
    },
    SET_LOGIN: (state, login) => {
      state.isLogin = login
      localStorage.setItem('isLogin', login)
    },
    SET_USERNAME: (state, username) => {
      state.username = username
      localStorage.setItem('username', username)
    },
    SET_USERID: (state, userId) => {
      state.user_id = userId
      localStorage.setItem(userId)
    },
    SET_ACCESS_TOKEN: (state, access_token) => {
      state.access_token = access_token
      localStorage.setItem('access_token', access_token)
    },
    SET_REFRESH_TOKEN: (state, refresh_token) => {
      state.refresh_token = refresh_token
      localStorage.setItem('refresh_token', refresh_token)
    }
  },
  actions: {
    login({commit}, payloads) {
      commit('SET_LOADING', true)
      axios
        .post(config.API_BASE_URI + 'auth', payloads)
        .then((r) => r.data)
        .then((data) => {
          commit('SET_LOADING', false)
          commit('SET_ACCESS_TOKEN', data.access_token)
          commit('SET_REFRESH_TOKEN', data.refresh_token)
        })
    }
  },
  modules: {
  }
})

<template>
  <div id="app">
    <div id="nav" v-if="isLoggedIn">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import CheckLogin from '@/mixins/CheckLogin'

export default {
    mixins: [CheckLogin],
    data() {
      return {
        isLoggedIn: false
      }
    },
    mounted() {
        if(CheckLogin.methods.checkLogin())
            this.isLoggedIn = true
    }
}
</script>

<template>
  <div id="app">
    <div id="nav" v-if="isLoggedIn">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  mounted() {
    if (localStorage.getItem('isLogin') == false) this.$router.push({name: 'Login'})
  }
};
</script>

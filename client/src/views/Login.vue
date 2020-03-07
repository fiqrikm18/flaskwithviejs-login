<template>
  <div class="container">
    <div>
      <form class="form" @submit="submit">
        <h2>User Login</h2>
        <div class="input-container">
          <i class="fa fa-user icon"></i>
          <input
            type="text"
            v-model="username"
            class="input-field"
            placeholder="Username"
          />
        </div>

        <div class="input-container">
          <i class="fa fa-key icon"></i>
          <input
            type="password"
            v-model="password"
            class="input-field"
            placeholder="Password"
          />
        </div>

        <button class="btn">
          <img v-if="isLoading" src="@/assets/loading.svg" />
          <p v-else>Login</p>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    submit(e) {
      e.preventDefault();
      let payloads = {
        username: this.username,
        password: this.password
      };
      this.$store.dispatch("login", payloads);
    }
  },
  computed: {
    ...mapState({
      isLoading: "isLoading",
      access_token: "access_token",
      refresh_token: "refresh_token"
    })
  }
};
</script>

<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-btn text> TODO </v-btn>

      <v-spacer></v-spacer>

      <v-btn text :to="{ name: 'Login' }" v-if="!isUserLoggedIn">
        <span class="mr-2">Login</span>
        <v-icon>mdi-login</v-icon>
      </v-btn>
      <v-btn text :to="{ name: 'Signup' }" v-if="!isUserLoggedIn">
        <span class="mr-2">Signup</span>
        <v-icon>mdi-login</v-icon>
      </v-btn>
      <v-btn text v-if="isUserLoggedIn" @click="logoutClicked">
        <span class="mr-2">Logout</span>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "App",

  data: () => ({}),
  computed: {
    ...mapGetters(["isUserLoggedIn"]),
  },
  methods: {
    ...mapActions(["logout"]),
    logoutClicked() {
      this.logout();
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

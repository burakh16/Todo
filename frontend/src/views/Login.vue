<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-row justify="center" class="mt-5">
      <v-col cols="8">
        <v-text-field
          outlined
          v-model="user.username"
          label="Username"
          :rules="[rules.required, rules.min]"
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-text-field
          outlined
          v-model="user.password"
          label="Password"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
          :rules="[rules.required, rules.min]"
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-btn @click="loginButtonClick()" class="float-right" color="primary"
          >Login</v-btn
        >
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data: () => ({
    showPassword: false,
    user: {
      username: "",
      password: "",
    },
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 5 || "Min 5 characters",
    },
  }),
  methods: {
    ...mapActions(["login"]),
    async loginButtonClick() {
      try {
        if (!this.validate) return;
        await this.login(this.user);
        this.$router.push({ name: "Home" });
      } catch (error) {
        console.log(error);
        this.$toast.error(error);
      }
    },
  },
  computed: {
    validate() {
      return this.$refs.form.validate();
    },
  },
};
</script>

<style>
</style>
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
          :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword1 ? 'text' : 'password'"
          @click:append="showPassword1 = !showPassword1"
          :rules="[rules.required, rules.min]"
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-text-field
          outlined
          v-model="user.password2"
          label="Password Repeat"
          :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword2 ? 'text' : 'password'"
          :rules="[rules.required, passwordsMatch]"
          @click:append="showPassword2 = !showPassword2"
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-btn @click="signupButtonClick()" class="float-right" color="primary"
          >Sign Up</v-btn
        >
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data: () => ({
    showPassword1: false,
    showPassword2: false,
    user: {
      username: "",
      password: "",
      password2: "",
    },
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 5 || "Min 5 characters",
    },
  }),
  methods: {
    ...mapActions(["signup"]),
    passwordsMatch() {
      if (this.user.password !== this.user.password2)
        return "Passwords don't match!";
      return true;
    },
    async signupButtonClick() {
      try {
        if (!this.validate) return;
        await this.signup(this.user);
        this.$toast.success("Your account created successfully.");
        this.$router.push({ name: "Login" });
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
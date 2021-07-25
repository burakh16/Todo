<template>
  <v-text-field
    v-model="todo"
    append-outer-icon="mdi-send"
    dense
    outlined
    label="New Todo"
    type="text"
    @click:append-outer="createTodoClick"
  ></v-text-field>
</template>

<script>
export default {
  data: () => ({
    todo: "",
  }),
  methods: {
    createTodoClick() {
      this.$emit("createButtonClicked", this.todo);
      this.todo = "";
    },
  },
};
</script>

<style>
</style>
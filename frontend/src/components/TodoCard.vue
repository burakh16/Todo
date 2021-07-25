<template>
  <v-card @dblclick="completeTodo()" :color="todo.status ? 'green' : ''">
    <v-card-text
      >{{ todo.description }}
      <small class="float-right">{{ todo.created_at }}</small>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    todo: {},
  },
  methods: {
    completeTodo() {
      this.$emit("completeTodo", this.todo);
    },
  },
};
</script>

<style>
</style>
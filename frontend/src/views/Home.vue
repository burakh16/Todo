<template>
  <v-row>
    <v-col cols="12">
      <new-todo @createButtonClicked="createButtonClick" />
    </v-col>
    <v-col cols="4" v-for="todo in getTodos">
      <todo-card :todo="todo" @completeTodo="completedTodo" />
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import TodoCard from "../components/TodoCard.vue";
import NewTodo from "../components/NewTodo.vue";

export default {
  name: "Home",
  components: {
    TodoCard,
    NewTodo,
    TodoCard,
  },
  computed: {
    ...mapGetters(["getTodos"]),
  },
  methods: {
    ...mapActions(["getTodosPaging", "createTodo", "completeTodo"]),

    async loadTodos() {
      await this.getTodosPaging();
    },

    async createButtonClick(todo) {
      try {
        await this.createTodo({ description: todo });
      } catch (error) {}
    },

    async completedTodo(todo) {
      try {
        await this.completeTodo(todo.id);
      } catch (error) {}
    },
  },
  async created() {
    await this.loadTodos();
  },
};
</script>

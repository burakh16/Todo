import axios from 'axios'

const state = {
    todos: [],
}

const getters = {
    getTodos: (state) => state.todos,
}

const actions = {
    async getTodosPaging({ commit }) {
        const response = await axios.get('todo/')
        commit('SET_TODOS', response.data)
    },
    async createTodo({ commit }, todo) {
        const response = await axios.post('todo/create/', todo)
        commit('SET_TODO', response.data)
    },
    async completeTodo({ commit }, todoId) {
        const response = await axios.post(`todo/complete/${todoId}/`, {})
        commit('UPDATE_TODO', response.data)
    }
}

const mutations = {
    SET_TODOS: (state, todos) => state.todos = todos,
    SET_TODO: (state, todo) => {
        state.todos.unshift(todo)
    },
    UPDATE_TODO: (state, todo) => {
        const index = state.todos.findIndex(_todo => _todo.id === todo.id);
        if (index !== -1) {
            state.todos.splice(index, 1, todo);
        }
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
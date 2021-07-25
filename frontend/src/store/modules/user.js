import axios from 'axios'

const state = {
    accessToken: '' || localStorage.getItem('access'),
    refreshToken: '' || localStorage.getItem('refresh'),
    3: {}
}

const getters = {
    getAccessToken: (state) => state.accessToken,
    getRefreshToken: (state) => state.refreshToken,
    isUserLoggedIn: (state) => !!state.accessToken
}

const actions = {
    async login({ commit }, user) {
        const response = await axios.post('user/token/', user)
        localStorage.setItem('access', response.data.access)
        localStorage.setItem('refresh', response.data.refresh)
        commit('SET_TOKEN', response.data)
    },
    async signup({ }, user) {
        await axios.post('user/create/', user)
    },
    async retriveRefreshToken({ commit }) {
        const response = await axios.post('user/token/refresh/', {
            'refresh': this.getters.getRefreshToken
        })
        localStorage.setItem('access', response.data.access)
        commit('SET_ACCESS_TOKEN', response.data)
    },
    logout({ commit }) {
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        commit('SET_TOKEN', { access: '', refresh: '' })
    }
}

const mutations = {
    SET_TOKEN: (state, token) => {
        state.accessToken = token.access
        state.refreshToken = token.refresh
    },
    SET_ACCESS_TOKEN: (state, token) => {
        state.accessToken = token.access
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
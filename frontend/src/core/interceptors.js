const axios = require('axios');
import store from '../store'
import router from '../router/index.js'

// Request interceptor for API calls
export default function setup() {
    axios.interceptors.request.use(
        async config => {
            config.baseURL = "http://localhost:8000/api/"
            const token = store.getters.getAccessToken;
            if (token)
                config.headers = {
                    'Authorization': `Bearer ${token}`,
                }
            return config;
        },
        error => {
            Promise.reject(error)
        });

    // Response interceptor for API calls
    axios.interceptors.response.use((response) => {
        return response
    }, async function (error) {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            await store.dispatch('retriveRefreshToken');
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + store.getters.getAccessToken;
            return axios(originalRequest);
        }
        else if (error.response.status === 400) {
            return Promise.reject(Object.values(error.response.data).join(','))
        }
        else if (error.response.status === 401 && originalRequest._retry) {
            router.push({ name: 'Login' })
        }
        return Promise.reject(error);
    });
}
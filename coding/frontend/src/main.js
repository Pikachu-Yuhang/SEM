import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as echarts from 'echarts'
import axios from 'axios'

const app = createApp(App);

axios.defaults.baseURL = 'http://localhost:5050';
app.config.globalProperties.$http = axios;

app.use(router).use(echarts).mount('#app');

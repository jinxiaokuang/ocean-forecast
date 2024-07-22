import { createApp } from 'vue'
import App from './App.vue'
import router from './modules/router'
import pinia from './modules/pinia'

import "./stores/leaflet.canvaslayer.field.js";
import L from "leaflet";
import 'leaflet/dist/leaflet.css';


const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(L)

app.mount('#app')


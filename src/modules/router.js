import { createRouter,createWebHistory } from "vue-router";
//import { routes as fileRoutes } from 'vue-router/auto-routes'

const router = createRouter({
    routes: [{
        name: '首页',
        'component': () => import('../pages/home.vue')


    }],
    history:createWebHistory()
})

export default router
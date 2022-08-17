import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue'
import Forgot from '../views/Forgot.vue'
import Settings from '../views/Settings.vue'
import Recipes from '../views/Recipes.vue'
import RecipePage from '../views/RecipePage.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/forgot',
        name: 'Forgot',
        component: Forgot
    },
    {
        path: '/settings',
        name: 'Settings',
        component: Settings
    },
    {
        path: '/recipes',
        name: 'Recipes',
        component: Recipes
    },
    {
        path: '/recipes/:id',
        name: 'RecipePage',
        component: RecipePage
    }
]
const router = new VueRouter({
    routes
})

export default router
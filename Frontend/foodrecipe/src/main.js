import Vue from 'vue'
import App from './App.vue';

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en';

import i18n from './i18n'

import router from './router';
import store from './store';

Vue.use(ElementUI);

new Vue({
    router,
    store,
    beforeCreate() {
        this.$store.dispatch('VerifyLogin').then((response) => {
            if (response == '200') {
                if (router.currentRoute.name == 'Login') {
                    router.push({ name: 'Home' });
                }
            } else {
                if (router.currentRoute.name != 'Login') {
                    router.push({ name: 'Login' });
                }
            }
        }).catch(() => {
            if (router.currentRoute.name != 'Login') {
                router.push({ name: 'Login' });
            }
        });
    },
    i18n,
    render: h => h(App),
}).$mount('#app')

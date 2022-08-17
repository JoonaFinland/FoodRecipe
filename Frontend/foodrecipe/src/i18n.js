import en from './assets/translations/en.json';
import fi from './assets/translations/fi.json';
import VueI18n from 'vue-i18n';
import Vue from 'vue';

Vue.use(VueI18n);

export default new VueI18n({
    locale: localStorage.getItem('lang') || 'en',
    fallbackLocale: 'en',
    messages: {
        en: en,
        fi: fi
    }
})
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        APIBaseUrl: "http://192.168.1.8:8000/",
        isLoggedIn: false,
        AccessToken: 'Bearer ',
        RefreshToken: 'Bearer ',
        UserProfile: '',
        NavBarExpanded: true,
        isMobile: false,
    },
    plugins: [
        createPersistedState()
    ],
    // HAVE REFRESH SAVED FOR FUTURE INCASE USE THOSE :D
    mutations: {
        CLEAR_STATE: (state) => {
            state.isLoggedIn = false;
            state.AccessToken = 'Bearer ';
            state.RefreshToken = 'Bearer ';
        },
        SET_LOGIN_FLAG: (state, flag) => {
            state.isLoggedIn = flag;
        },
        SET_ACCESS_TOKEN: (state, token) => {
            state.AccessToken = token;
        },
        SET_REFRESH_TOKEN: (state, token) => {
            state.RefreshToken = token;
        },
        SET_PROFILE: (state, data) => {
            state.UserProfile = data;
        },
        TOGGLE_EXPAND: (state) => {
            state.NavBarExpanded = !state.NavBarExpanded;
        }
    },
    actions: {
        async VerifyLogin(context) {
            return new Promise((resolve, reject) => {
                
                axios.post(context.state.APIBaseUrl + "api/verifytoken", { token: context.state.AccessToken }, {
                    headers: { Authorization: "JWT " + context.state.AccessToken }
                }).then(response => {
                    if (response.status == "200") {
                    resolve(response.status);
                    console.log("logged in")
                    }
                })
                    .catch(async function (error) {
                    // request failed 
                    reject(error) // return error to calling function
                    })
            });

        },
        ToggleExpand(context) {
            context.commit("TOGGLE_EXPAND");
        },
        Login(context, credentials) {
            console.log('inside login')
            console.log(context.state.APIBaseUrl + "api/login")
            return new Promise((resolve, reject) => {
                axios.post(context.state.APIBaseUrl + "api/login", credentials)
                .then(response => {
                    console.log(response);
                    if (response.status == "200") {
                        context.commit("SET_ACCESS_TOKEN", response.data.access);
                        context.commit("SET_LOGIN_FLAG", true);
                        resolve();
                        /*context.dispatch("FetchProfile")
                            .then(() => {
                                context.commit("SET_LOGIN_FLAG", true);
                                resolve();
                            })*/
                    }
                })
                .catch(error => {
                    console.log(error);
                    reject(error);
                })
            });
        },
        Logout(context) {
            context.commit("CLEAR_STATE")
        },
        FetchProfile(context) {
            return new Promise((resolve) => {
                axios.get(context.state.APIBaseUrl + "api/user", {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    context.commit("SET_PROFILE", response.data);
                    resolve(response.data);
                })
            })
        },
        GetRecipes(context) {
            return new Promise((resolve) => {
                axios.get(context.state.APIBaseUrl + "api/recipe/all", {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
            })
        },
        GetIngredients(context) {
            return new Promise((resolve) => {
                axios.get(context.state.APIBaseUrl + "api/ingredient/all", {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
            })
        },
        CreateRecipe(context, payload) {
            return new Promise((resolve, reject) => {
                axios.get(context.state.APIBaseUrl + "api/recipe/create", payload, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    if (response.status == "200") {
                        resolve(response.data);
                    }
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
        CreateIngredient(context, payload) {
            return new Promise((resolve, reject) => {
                axios.get(context.state.APIBaseUrl + "api/ingredient/create", payload, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    if (response.status == "200") {
                        resolve(response.data);
                    }
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
        GetRecipeByID(context, id) {
            return new Promise((resolve) => {
                axios.get(context.state.APIBaseUrl + "api/recipe/" + id, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
            })
        },
        DeleteRecipe(context, id) {
            return new Promise((resolve, reject) => {
                axios.delete(context.state.APIBaseUrl + "api/recipe/" + id, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
        UpdateRecipe(context, payload) {
            return new Promise((resolve, reject) => {
                axios.patch(context.state.APIBaseUrl + "api/recipe/" + payload.id, payload.body, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
        GetIngredientByID(context, id) {
            return new Promise((resolve) => {
                axios.get(context.state.APIBaseUrl + "api/ingredient/" + id, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
            })
        },
        DeleteIngredient(context, id) {
            return new Promise((resolve, reject) => {
                axios.delete(context.state.APIBaseUrl + "api/ingredient/" + id, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
        UpdateIngredient(context, payload) {
            return new Promise((resolve, reject) => {
                axios.patch(context.state.APIBaseUrl + "api/ingredient/" + payload.id, payload.body, {
                    headers: { Authorization: "Bearer " + context.state.AccessToken }
                })
                .then(response => {
                    resolve(response.data);
                })
                .catch(error => {
                    reject(error);
                })
            })
        },
    }
})
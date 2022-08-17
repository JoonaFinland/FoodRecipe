<template>
  <div id="navbar" class="no-top-left-margin" :style="{ width: getWidth() }">
    <div class="navbar-logo" v-if="sideBarToggle">
      <img class="normal-logo" src="../assets/logo.png" />

      <div id="wudpecker-heading">{{ $t('foodrecipe') }}</div>
      <!--  <div id="user-info">
            <div id="username">
              {{ $store.state.UserProfile.user.first_name }}
              {{ $store.state.UserProfile.user.last_name }}
            </div>
            <div id="company">Wudpecker</div>
          </div> -->
    </div>
    <div class="navbar-logo-small" v-else>
      <img class="small-logo" src="../assets/logo.png" />

      <!--  <div id="user-info">
            <div id="username">
              {{ $store.state.UserProfile.user.first_name }}
              {{ $store.state.UserProfile.user.last_name }}
            </div>
            <div id="company">Wudpecker</div>
          </div> -->
    </div>

    <div id="item-list">
      <router-link to="/">
        <div :class="
            active === 'Home' ? 'active-menu-item menu-item' : 'menu-item'
          ">
          <div :class="
              active === 'Home'
                ? 'menu-item-icon menu-item-icon-selected'
                : 'menu-item-icon'
            ">
            <i class="el-icon-s-home"></i>
          </div>
          <div v-if="sideBarToggle">{{ $t('home') }}</div>
        </div>
      </router-link>

      <router-link to="/recipes">
        <div :class="
            active === 'Recipes' ? 'active-menu-item menu-item' : 'menu-item'
          ">
          <div :class="
              active === 'Recipes'
                ? 'menu-item-icon menu-item-icon-selected'
                : 'menu-item-icon'
            ">
            <i class="el-icon-tableware"></i>
          </div>
          <div v-if="sideBarToggle">{{ $t('recipes') }}</div>
        </div>
      </router-link>

      <!-- 
      <router-link to="/analysis">
        <div :class="active === 'Analysis' ? 'active-menu-item menu-item' : 'menu-item'">
    
              <div :class="active === 'Analysis' ? 'menu-item-icon menu-item-icon-selected' : 'menu-item-icon'">
                <i class="el-icon-s-data"></i>
              </div>

            <div> Analysis </div>
        
        </div>
      </router-link> -->
      <router-link to="/settings">
        <div :class="
            active === 'Settings' ? 'active-menu-item menu-item' : 'menu-item'
          ">
          <div :class="
              active === 'Settings'
                ? 'menu-item-icon menu-item-icon-selected'
                : 'menu-item-icon'
            ">
            <i class="el-icon-s-tools"></i>
          </div>

          <div v-if="sideBarToggle">{{ $t('settings') }}</div>
        </div>
      </router-link>

      <div @click="logout" :class="
          active === 'Logout' ? 'active-menu-item menu-item' : 'menu-item'
        ">
        <div class="menu-item-icon">
          <i class="el-icon-remove"></i>
        </div>

        <div v-if="sideBarToggle">{{ $t('logout') }}</div>
      </div>
    </div>

    <div id="language-section" :class="sideBarToggle ? 'lang-open' : 'lang-close'">
      <!--<el-select v-model="language">
        <el-option
          v-for="lang in langOptions"
          :key="lang.value"
          :label="lang.label"
          :value="lang.value">
          <span><country-flag :country="lang.value" size="medium"/>
          <p>{{ lang.label }}</p></span>
        </el-option>
      </el-select>-->
      <el-dropdown>
        <span class="el-dropdown-link">
          <country-flag :country="language.value" size="normal" /><i class="el-icon-arrow-down"></i>
          <!--<i class="el-icon-arrow-down el-icon--right"></i>-->
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item
            v-for="lang in langOptions"
            :key="lang.value"
            v-on:click.native="changeLang(lang)">
            <country-flag :country="lang.value" size="normal" />
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>

    <div id="user-info-section">
      <i class="el-icon-d-arrow-right close-icon" :class="{ 'rotate-180': sideBarToggle }" v-on:click="toggleSideBar()"></i>
      <div v-if="sideBarToggle" class="user-profile">
        <el-avatar id="logo-nav-img" icon="el-icon-user-solid"></el-avatar>
        
      </div>
      <div v-if="sideBarToggle" class="user-profile">
        <div style="font-size: 14px; font-weight: bold">
          First Last
        </div>
          <!--<div style="font-size: 14px; font-weight: bold">
            {{ $store.state.UserProfile.user.first_name }}
            {{ $store.state.UserProfile.user.last_name }}
          </div>
          <div style="font-size: 12px">
            {{ $store.state.UserProfile.company_domain }}
          </div>-->
      </div>
    </div>
  </div>
</template>

<script>
import CountryFlag from 'vue-country-flag';
export default {
  name: "NavBar",
  components: {
    CountryFlag,
  },
  data() {
    return {
      active: this.$router.currentRoute.name,
      sideBarToggle: true,
      locale: this.$i18n.locale,
      language: {value: "us", label: 'English'},
      langOptions: [{value: "us", label: 'English'}, {value: "fi", label: 'Suomi'}],
    };
  },
  mounted() {
    this.locale = this.$i18n.locale;
    let storage_lang = this.locale
    this.language = {
      value: storage_lang,
      label: storage_lang=='en' ? 'English' : 'Suomi'
    }
  },
  watch: {
    $route(to) {
      this.active = to.name;
    },
    locale(val) {
      this.$i18n.locale = val;
    }
  },

  methods: {
    goto: function (path_name) {
      window.location.href = this.$router.resolve({
        name: path_name,
        // params: { id: some_id, slug: some_slug },
      }).href;

      //this.$router.push({ name: path_name });
      //this.active = path_name;
    },
    logout: function () {
      console.log("Logging out");
      this.$store.dispatch("Logout").then(() => {
        window.open(
          this.$router.resolve({
            name: "Login",
            // params: { id: some_id, slug: some_slug },
          }).href,
          "_self"
        );
      });
    },
    toggleSideBar() {
      this.sideBarToggle = !this.sideBarToggle;
      this.$store.dispatch("ToggleExpand")
      this.$emit('toggleBar');

    },
    getWidth() {
      const WIDTH = 250;
      const WIDTH_COLL = 100;
      return `${this.sideBarToggle ? WIDTH : WIDTH_COLL}px`;
    },
    changeLang(lang) {
      this.language = lang;
      this.locale = lang.value;
      localStorage.setItem('lang', this.language.value);
    },
  }
};
</script>
<style>
.el-avatar {
  background: white !important;
  /* color: rgba(var(--vs-primary), 1) !important; */
  color: black !important;
}
</style>

<style scoped>
.el-dropdown-link {
  cursor: pointer;
}
.lang-open {
  padding-left: 30px;
  transition: 0.2s linear;
}
.lang-close {
  padding-left: 30px;
  transition: 0.2s linear;
}
.el-icon-arrow-down {
  font-size: 1.4em;
}
#navbar {
  position: fixed;
  height: 100vh;
  /* background: rgba(var(--vs-primary), 1); */
  background: #1d1d1c;
  margin-right: 0px;
  color: #8d969d;
  overflow: hidden;
  transition: 0.2s linear;
}

.user-profile {
  display: inline-block;
  transition:opacity 1s linear;
}

#language-section {
  position: absolute;
  display: flex;
  cursor: pointer;
  width: 100%;
  align-items: center;
  bottom: 120px;
  height: 75px;
}
.close-icon {
  font-size: 2.5em;
  margin-right: 25px;

  transition: 0.2s linear;
}
.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.navbar-logo {
  display: flex;
  flex-direction: row;
  align-items: center;
  color: white;

  margin-top: 20px;
  text-align: center;
  background: rgba(182, 182, 182, 0.05);
  margin-left: 20px;
  margin-right: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 25px;
  transition: 0.2s linear;
  border-radius: 5px;
}

.navbar-logo-small {
  display: flex;
  flex-direction: row;
  align-items: center;
  color: white;

  margin-top: 20px;
  text-align: center;
  background: rgba(182, 182, 182, 0.05);
  margin-left: 20px;
  margin-right: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 12px;
  transition: 0.2s linear;
  border-radius: 5px;
}

#logo-nav-img {
  width: 40px;
  margin-right: 10px;
  transition: 0.2s linear;
}
.normal-logo {
  width: 40px;
  margin-right: 10px;
  transition: 0.2s linear;
}
.small-logo {
  width: 40px;
  margin-right: 10px;
  align-items: center;
  transition: 0.2s linear;
}

#wudpecker-heading {
  font-size: 1.2em;
  font-weight: bold;
}

#user-info-details {
  align-items: center;
}

#user-info-section {
  position: absolute;
  display: flex;
  cursor: pointer;
  width: 100%;
  align-items: center;
  bottom: 30px;
  padding-left: 25px;
  transition:opacity 1s linear;
}

#item-list {
  margin-top: 40px;

  font-size: 1em;
  font-weight: bold;
}

.menu-item {
  display: flex;
  flex-direction: row;
  align-items: center;

  padding-left: 30px;
  padding-bottom: 12px;
  padding-top: 12px;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-family: Work Sans, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue,
    Arial, sans-serif !important;
  font-size: 0.875rem;
  font-weight: 600;
  transition: 0.2s linear;
}

.menu-item:hover {
  cursor: pointer;
  color: white;
}

.active-menu-item {
  color: white;
}

.menu-item-icon {
  border-radius: 50px;
  padding: 8px;
  vertical-align: middle;
  margin-right: 20px;
  font-size: 1.3em;
  transition: 0.2s linear;
}

.lang-icon {
  border-radius: 50px;
  padding: 8px;
  margin-right: 20px;
  font-size: 1.3em;
}

.menu-item-icon-selected {
  background: rgba(87, 90, 97, 0.5);
}

#user-info {
  text-align: left;
}

#username {
  font-size: 1.05em;
  font-weight: bold;
}
</style>

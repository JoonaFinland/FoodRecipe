<template>
  <div id="navbarmobile" class="mobile-menu">
    <el-row>
      <el-col :span="22">
        <h1 style="padding-left: 50px; margin-top: 15px;">{{ $t('foodrecipe') }}</h1>
      </el-col>
      <el-col :span="2">
        <i class="el-icon-menu large-menu" @click="clickMenu()"></i>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  components: {
  },
  data() {
    return {
      active: this.$router.currentRoute.name,
      sideBarToggle: true,
      language: {value: "us", label: 'English'},
      langOptions: [{value: "us", label: 'English'}, {value: "fi", label: 'Suomi'}],
    };
  },
  mounted() {
    let storage_lang = localStorage.getItem('lang') || 'en';
    this.language = {
      value: storage_lang,
      label: storage_lang=='en' ? 'English' : 'Suomi'
    }
  },
  watch: {
    $route(to) {
      this.active = to.name;
    },
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
      localStorage.setItem('lang', this.language.value);
      window.location.reload();
    },
    clickMenu() {
      this.$emit('clickMenu');
    }
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
.mobile-menu {
  width: 100%;
  color: #d4d4d4;
}

.large-menu {
  margin-top: 18px;
  padding-right: 30px;
  font-size: 2em;
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

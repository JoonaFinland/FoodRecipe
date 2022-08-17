<template>
    <div
        id="app"
    >
          <!-- v-if="!$store.state.isMobile"-->
          <div
              id="main-container"
              v-if="this.$router.currentRoute.name != 'Login' &&
                  this.$router.currentRoute.name != 'Forgot'
              "
          >
              <el-header v-if="$store.state.isMobile" style="width: 100%; background-color: #1d1d1c; height: 70px ">
                  <nav-bar-mobile @clickMenu="onClickMenu"/>
              </el-header>
              <el-aside v-else :style="{ width: getWidth() }" style="overflow: visible">
                  <nav-bar @toggleBar="onToggleBar"/>
              </el-aside>

              
              <!--<headerbar />-->
              
              <!--<div v-if="centerDialogVisible && $store.state.isMobile" class="scrollable">
                <nav-bar-dialog @clickExit="onClickExit"/>
              </div>

              <div v-else class="scrollable">
                <el-main v-if="!$store.state.isMobile" id="main-section" :style="{ 'margin-left': getWidth() }">
                    <router-view :key="$route.fullPath" />
                </el-main>

                <el-main v-else id="main-section">
                    <router-view :key="$route.fullPath" />
                </el-main>
              </div>-->


              <el-main v-if="!$store.state.isMobile && !centerDialogVisible" class="main-section" :style="{ 'margin-left': getWidth() }">
                  <router-view :key="$route.fullPath" />
              </el-main>

              <el-main v-if="$store.state.isMobile && !centerDialogVisible" class="main-section-mobile">
                  <router-view :key="$route.fullPath" />
              </el-main>

              <el-main v-if="centerDialogVisible && $store.state.isMobile">
                <nav-bar-dialog @clickExit="onClickExit" style="position: absolute;left:0px;top:0px;"/>
              </el-main>
              <!--<nav-bar-dialog v-if="centerDialogVisible && $store.state.isMobile" @clickExit="onClickExit"/>-->

          </div>

          <el-container v-else>
              <router-view />
          </el-container>
    </div>
</template>

<script>

import NavBar from "./components/NavBar.vue";
import NavBarMobile from "./components/NavBarMobile.vue";
import NavBarDialog from "./components/NavBarDialog.vue";

export default {
    name: "App",
    components: {
        NavBar,
        NavBarMobile,
        NavBarDialog,
    },
    data() {
      return {
        width: "250px",
        padding: "250px",
        sideBarToggle: true,
        centerDialogVisible: false,
      };
    },
    methods: {
      getWidth() {
        return this.width;
      },
      getPadding() {
        return this.padding;
      },
      onToggleBar() {
        this.sideBarToggle = !this.sideBarToggle;
        const WIDTH = 250;
        const WIDTH_COLL = 100;
        this.width = `${this.sideBarToggle ? WIDTH : WIDTH_COLL}px`;
      },
      onClickMenu() {
        this.centerDialogVisible = true;
        console.log("openede mobile")
      },
      onClickExit() {
        this.centerDialogVisible = false;
        console.log("closede mobile")
      },
      onResizeMount() {
        this.$store.state.isMobile = window.innerWidth*2/3 < 690;
        //this.$store.state.isMobile = true;
      },
      onResize() {
        this.$store.state.isMobile = window.innerWidth < 690;
        //this.$store.state.isMobile = true;
      }
    },
    beforeMount() {
      document.title = this.$t('foodrecipe');
    },
    mounted() {
      this.onResizeMount();
      window.addEventListener("resize", this.onResize, { passive: true });
    },
    beforeDestroy () {
      if (typeof window !== 'undefined') {
        window.removeEventListener("resize", this.onResize, { passive: true });
      }
    }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Nunito:regular,bold,Extra-bold");
@import url("https://fonts.googleapis.com/css?family=Space+Grotesk:regular,bold,Extra-bold");
@import url("https://fonts.googleapis.com/css?family=Work+Sans:regular,bold,Extra-bold");

.white-bg {
  background: white !important;
}
#app {
  /* font-family: Nunito, Helvetica, Arial, sans-serif; */
  /*  font-family: Space Grotesk, Helvetica, Arial, sans-serif; */
  font-family: "Work Sans", BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1d1d1c;
  text-align: left;
  background: #dee9eb;
  height: 100vh;
  overflow: hidden;
}
.el-dialog__close {
  font-size: 2.5em !important;
}
a {
  text-decoration: none;
  color: inherit;
}
.no-top-left-margin {
    margin-top: 0px !important;
}

body {
  margin-top: 0px !important;
  margin-left: 0px !important;
  margin-bottom: 0px !important;
  margin-right: 0px !important;
}

.page-heading {
  margin-top: 0px;
  margin-left: 20px;
  padding-right: 10px !important;
  padding-left: 0px;
  height: 100%;
  overflow: auto;
  font-size: 2em;
  margin-top: 0px;
  margin-bottom: 40px;
  font-weight: bold;
  font-family: Space Grotesk, Helvetica, Arial, sans-serif;
}

.page-heading-mobile {
  margin-top: 0px;
  margin-left: 0px;
  padding-right: 10px !important;
  padding-left: 0px;
  height: 100%;
  overflow: auto;
  font-size: 1.5em;
  margin-top: 0px;
  margin-bottom: 40px;
  font-weight: bold;
  font-family: Space Grotesk, Helvetica, Arial, sans-serif;
}

.main-section {
  margin-top: 0px;
  margin-left: 0px;
  padding-right: px !important;
  padding: 0px;
  padding-left: 5px;
  height: 100%;
  overflow: auto;
}

.main-section-mobile {
  margin-top: 0px;
  position: absolute;
  margin-left: 0px;
  padding-right: px !important;
  padding: 0px;
  height: 100%;
  overflow: auto;
}

.page-heading-base {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: space-between;
}

.page-sub-heading {
  font-size: 1.25em;
  font-weight: bold;
  margin-bottom: 25px;
  margin-top: 10px;
  font-family: Space Grotesk, Helvetica, Arial, sans-serif;
  text-align: left !important;
}

.card-small-heading {
  font-size: 0.8em;
  margin-top: 10px;
  cursor: pointer;
}

.card-small-heading:hover {
  text-decoration: underline;
}

.card-med-heading {
  margin-top: 20px;
  margin-bottom: 15px;
  font-size: 0.9em;
}

.card-big-heading {
  font-size: 2.5em;
  font-weight: bold;
}

.page-content {
  overflow: scroll;
  max-height: 100%;
}

#main-container {
  height: 100vh;
}
</style>

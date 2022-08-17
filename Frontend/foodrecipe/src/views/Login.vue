<template>
  <div id="login-view">
    <!--class="login-card"-->
    <el-card :class="$store.state.isMobile ? 'login-card-mobile' : 'login-card'" shadow="hover">
      <div slot="header" class="clearfix">
        <h1 style="text-align: center">Log in</h1>
      </div>

      <div id="id-pass" class="login-area">
        <el-form
          label-position="top"
          :model="loginForm"
          ref="loginForm"
          label-width="120px"
          class="login-form"
        >
          <el-form-item label="Email">
            <el-input
              v-model="loginForm.username"
              @keyup.enter.native="manual_login"
            ></el-input>
          </el-form-item>
          <el-form-item label="Password">
            <el-input
              type="password"
              v-model="loginForm.password"
              autocomplete="off"
              @keyup.enter.native="manual_login"
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button
              style="width: 100%; height: 50px"
              type="primary"
              @click="manual_login"
              :loading="isLoginButtonLoading"
              ><b>Login</b></el-button
            >
          </el-form-item>
        </el-form>

        <div
          id="login-error"
          style="color: red; text-align: center; margin-top: 20px"
          v-if="LoginError"
        >
          <i style="margin-right: 10px" class="el-icon-warning-outline"></i
          >Email or Password is incorrect. Try again. Slowly this time?
        </div>
      </div>
    </el-card>
  </div>
</template>


<script>
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
        error: "",
      },
      isLoginButtonLoading: false,
      LoginError: false,
    };
  },

  methods: {
    manual_login() {
      this.isLoginButtonLoading = true;
      console.log("attempting logging in");
      this.$store
        .dispatch("Login", this.loginForm)
        .then(() => {
          console.log('inside manual then')
          window.open(
            this.$router.resolve({
              name: "Home",
              // params: { id: some_id, slug: some_slug },
            }).href,
            "_self"
          );
        })
        .catch(() => {
          this.LoginError = true;
          this.isLoginButtonLoading = false;
        });
    }
  },
  beforeMount() {
    document.title = this.$t('foodrecipe');
  },
};
</script>

<style scoped>
#login-view {
  width: 70%;
  margin: auto;
  margin-top: 50px;
  font-family: Space Grotesk, Helvetica, Arial, sans-serif;
}
.login-card {
  padding-left: 15%;
  padding-right: 15%;
  padding-bottom: 30px;
}
.login-card-mobile {
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 30px;
}
.login-area {
  width: 90%;
  max-width: 350px;
  margin: auto;
}

#oauth {
  margin-top: 35px;
}

#id-pass {
  margin-bottom: 35px;
}

.invisible-button {
  background: none;
  border: none;
  font-weight: bold;
  font-size: 16px;
  color: #303133;
  font-family: Nunito;
}

#form-extra {
  margin-top: 25px;
  margin-bottom: 30px;
  text-align: center;
}
.login-button-options {
  margin-bottom: 25px;
}
</style>


<style>
#id-pass .el-form-item {
  margin-bottom: 10px;
}
#id-pass .el-form-item__label {
  padding: 0px !important;
  font-weight: bold;
  color: black;
}

#id-pass .el-button--primary {
  margin-top: 20px;
}
</style>
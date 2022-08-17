<template>
  <div id="login-view">
    <el-card shadow="hover">
      <div slot="header" class="clearfix">
        <h3>Forgot password</h3>
      </div>

      <el-form
        ref="form"
        :model="form"
        label-width="120px"
        label-position="top"
      >
        <el-form-item label="Email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>

        <br />

        <el-form-item>
          <el-button
            type="primary"
            :loading="isLoginButtonLoading"
            @click="onSubmit"
            style="width: 100%; height: 50px"
            ><b>Forgot password</b></el-button
          >
        </el-form-item>
        {{ form.error }}
      </el-form>

      <div id="form-extra">
        <br />
        <b>Our privacy policy </b>
      </div>
    </el-card>
  </div>
</template>


<script>
export default {
  name: "Reset",
  data() {
    return {
      form: {
        username: "",
        password: "",
        error: "",
      },
      isLoginButtonLoading: false,
    };
  },

  methods: {
    onSubmit() {
      this.isLoginButtonLoading = true;
      this.$store
        .dispatch("Forgot", {
          email: this.form.email,
        })
        .then(() => {
          this.isLoginButtonLoading = false;
          this.form.error = "If your email is valid, an email will be sent to reset your password.";
        });
    },
  },
  beforeMount() {
    document.title = this.$t('foodrecipe');
  },
};
</script>

<style scoped>
#login-view {
  max-width: 450px;
  margin: auto;
  margin-top: 100px;
}

#form-extra {
  margin-top: 25px;
  margin-bottom: 30px;
  text-align: center;
}
</style>
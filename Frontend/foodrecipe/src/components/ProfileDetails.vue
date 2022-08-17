<template>
  <div id="profile-detail">
    <div id="account-details">
      <el-card class="wp-card" shadow="never">
        <div class="page-sub-heading">Personal details</div>
        <div id="account-info">
          <div class="account-info-entry">
            <div class="account-info-label">Email</div>
            <div class="account-info-value">
              {{ p.pr.user.email }}
            </div>
          </div>

          <div class="account-info-entry">
            <div class="account-info-label">Company domain</div>
            <div class="account-info-value">
              {{ p.pr.company_domain }}
            </div>
          </div>
          <el-button type="primary" @click="isResetDialogOpen = true">
            Reset password
          </el-button>
        </div>
      </el-card>
    </div>

    <div id="detail-reset">
      <el-card class="wp-card" shadow="never">
        <div class="page-sub-heading">Basic settings</div>
        <div id="account-info">
          <div class="account-info-entry">
            <div class="account-info-label">Meeting language</div>
            <div class="account-info-value">
              <div class="form-field">
                <div class="form-input">
                  <el-radio-group
                    v-model="language_word"
                    @change="optionChange"
                  >
                    <el-radio-button label="Swedish"></el-radio-button>
                    <el-radio-button label="English"></el-radio-button>
                  </el-radio-group>
                </div>
              </div>
            </div>
          </div>

          <div class="account-info-entry">
            <div class="account-info-label">Difficulty level</div>
            <div class="account-info-value">
              <div class="form-field">
                <div class="form-input">
                  <el-radio-group
                    v-model="p.pr.threshold"
                    @change="optionChange"
                  >
                    <el-radio-button label="Low"></el-radio-button>
                    <el-radio-button label="High"></el-radio-button>
                  </el-radio-group>
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-card>
    </div>

    <div id="team-details">
      <el-card class="wp-card" shadow="never">
        <div class="page-sub-heading">Team members</div>
        <div id="account-info">
          <el-table :data="getTeamMembers()" style="width: 100%">
            <el-table-column width="70">
              <el-avatar icon="el-icon-user-solid"></el-avatar>
            </el-table-column>
            <el-table-column prop="name" label="Name" width="400">
            </el-table-column>
            <el-table-column prop="email" label="Email" width="220">
            </el-table-column>
            <el-table-column prop="role" label="Role"> </el-table-column>
          </el-table>
        </div>
      </el-card>
    </div>

    <el-dialog
      title="Edit Meeting type"
      :visible.sync="isResetDialogOpen"
      width="30%"
      center
    >
      <div id="reset-f">
        <el-form
          label-position="top"
          :model="passwords"
          ref="resetForm"
          label-width="120px"
          class="reset-form"
        >
          <el-form-item label="Current password">
            <el-input
              v-model="passwords.old"
              type="password"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="New password">
            <el-input
              type="password"
              v-model="passwords.new"
              autocomplete="off"
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button
              style="width: 100%; height: 50px"
              type="primary"
              @click="changePassword"
              :loading="isResetLoading"
              ><b>Reset password</b></el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "ProfileDetail",
  data() {
    return {
      p: { pr: { user: {} } },
      isSaveButtonLoading: false,
      isResetDialogOpen: false,
      isResetLoading: false,
      server: "North Europe",
      language_word: "",
      passwords: {
        old: "",
        new: "",
      },
    };
  },
  methods: {
    changePassword: function () {
      this.isResetLoading = true;

      this.$store.dispatch("ResetPassword", this.passwords).then(() => {
        this.isResetLoading = false;
        this.passwords.old = "";
        this.passwords.new = "";
        this.isResetDialogOpen = false;
      });
    },
    optionChange() {
      let mapping = { English: "en-US", Swedish: "sv-SE" };
      this.p.pr.language = mapping[this.language_word];
      this.isSaveButtonLoading = true;
      this.$store
        .dispatch("PatchProfile", {
          first_name: this.p.pr.user.first_name,
          last_name: this.p.pr.user.last_name,
          email: this.p.pr.user.email,
          bio: this.p.pr.bio,
          location: this.p.pr.location,
          language: this.p.pr.language,
          threshold: this.p.pr.threshold,
        })
        .then(() => {
          this.isSaveButtonLoading = false;
        });
    },
    onSubmit: function () {
      this.isSaveButtonLoading = true;
      this.$store
        .dispatch("PatchProfile", {
          first_name: this.p.pr.user.first_name,
          last_name: this.p.pr.user.last_name,
          email: this.p.pr.user.email,
          bio: this.p.pr.bio,
          location: this.p.pr.location,
          language: this.p.pr.language,
          threshold: this.p.pr.threshold,
        })
        .then(() => {
          this.isSaveButtonLoading = false;
        });
    },
    getTeamMembers() {
      // TODO: properly loop later when Team members implemented
      return [
        {
          name: this.p.pr.user.first_name + " " + this.p.pr.user.last_name,
          email: this.p.pr.user.email,
          role: "Account Manager",
        },
      ];
    },
  },
  beforeMount() {
    this.$store.dispatch("Fetch_Profile2").then((data) => {
      this.p = { pr: data };
      let mapping = { "en-US": "English", "sv-SE": "Swedish" };
      this.language_word = mapping[this.p.pr.language];
    });
  },
};
</script>

<style scoped>
#profile-detail {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -moz-flex;
  display: -webkit-flex;
  display: flex;
  flex-wrap: wrap;
  max-height: 100%;
  width: 100%;
  align-items: flex-start;
  align-content: flex-start;
}
#account-details {
  width: 500px;
}

#detail-reset {
  width: 600px;
}
.form-label {
  margin-bottom: 15px;
  font-weight: bold;
}

#team-details {
  width: 100%;
}

.account-info-entry {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 25px;
}

.account-info-label {
  font-weight: 500;
}
.form-input {
  width: 100%;
}

#profile-page-content {
  max-width: 800px;
  margin: auto;
}

#profile-page-content > .el-row {
  margin-top: 20px;
}

.property-name {
  font-weight: bold;
}

#save-changes {
  width: 100%;
  margin-top: 25px;
  text-align: right;
}
</style>


<style>
#reset-f {
  text-align: left;
}
#reset-f .el-form-item {
  margin-bottom: 10px;
}
#reset-f .el-form-item__label {
  padding: 0px !important;
  font-weight: bold;
  color: black;
}

#reset-f .el-button--primary {
  margin-top: 20px;
}
</style>
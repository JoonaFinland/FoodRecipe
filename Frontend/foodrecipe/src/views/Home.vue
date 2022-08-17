<template>
    <div id="home">
        Home
    </div>
</template>

<script>

export default {
    name: "Home",
    components: {
    },
    methods: {
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
        }
    },
    beforeMount() {
        document.title = this.$t('foodrecipe');
    },
};
</script>

<style scoped>
#home {
  height: 100%;
}

#recent-meeting {
  min-width: 550px;
  width: 50%;
}
.activity-entry {
  text-align: center;
  padding-bottom: 30px;
  padding-top: 30px;
}

.activity-entry:hover {
  background: rgb(255, 245, 245);
  cursor: pointer;
}

.activity-value {
  font-size: 2.5em;
  font-weight: 900;
}

.meeting-activity-row {
  font-size: 15px;
  padding-bottom: 15px;
}

.rec-meeting {
  display: flex;
  flex-direction: row;
  cursor: pointer;
  align-items: center;

  flex-wrap: wrap;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 10px;
  border-radius: 5px;
}

.rec-meeting > div {
  margin-right: 30px;
}

.rec-title {
  max-width: 300px;
}

.rec-meeting:hover {
  background: #dee9eb;
}

.rec-icon {
  font-size: 1.25em;
}

.rec-info {
  font-size: 0.75em;
  display: flex;
  flex-direction: row;
}

#home-page-content {
  width: 100%;
}

#home-page-content > div {
  display: flex;
  flex-direction: row;
}

#score-card {
  width: 50%;
  min-width: 400px;
  text-align: center;
}

.small-card {
  cursor: pointer;
  width: 33.3%;
}

#credit-rem-bar {
  margin-right: 20px;
}

.lds-hourglass {
  margin: auto;
  margin-top: 50px;
  margin-left: 50px;
  width: 100%;
  height: 80px;
}
.lds-hourglass:after {
  content: " ";
  display: block;
  border-radius: 50%;
  width: 0;
  height: 0;
  margin: 8px;
  box-sizing: border-box;
  border: 32px solid rgb(var(--vs-primary));
  border-color: rgb(var(--vs-primary)) transparent rgb(var(--vs-primary))
    transparent;
  animation: lds-hourglass 1.2s infinite;
}
.test {
    border: 3px dotted gold;
}
</style>

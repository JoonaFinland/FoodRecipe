<template>
  <div id="meeting-card">
    <el-card :class="$store.state.isMobile ? 'box-card-mobile': 'box-card'" shadow="hover" body-style="padding: 0px">
        <!-- <b>{{ MeetingObject.title }}</b> -->
      <img :src="RecipeObject.img" :alt="RecipeObject.name" class="recipe-image">
      <div class="card-body clearfix">
        <div class="meeting-text">
          <b>{{ RecipeObject.name }}</b>
        </div>
        <div class="meeting-text-desc">
          {{ RecipeObject.details }}
        </div>
        <!--<div id="meeting-title">
          <i class="el-icon-time"> </i>
          {{ getTotalTime() }} {{ $t('minutes') }}
        </div>-->
        <div id="meeting-title">
          <i class="el-icon-user"> </i>
          {{ getPortions() }} {{ $t('portions') }}
        </div>
        <div class="meeting-tags">
          <el-tag
              v-for="tag in getTags()"
              :key="tag"
              class="people-attend"
              type="info"
              effect="dark"
              size="small"
          >
            {{tag}}
          </el-tag>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "MeetingCard",
  props: {
    RecipeObject: Object
  },

  methods: {
    getTags() {
      let tags = this.RecipeObject.tags.split(",");
      if (tags[0] == '') {
        return []
      }
      return this.RecipeObject.tags.split(",");
    },
    getTotalTime() {
      let totaltime = 0;
      this.RecipeObject.foods.forEach(food => {
        totaltime += food.time;
      })
      return totaltime;
    },
    getPortions() {
      let portions = [];
      this.RecipeObject.foods.forEach(food => {
        portions.push(food.portions);
      })
      return portions[0];
    }
  },
};
</script>

<style scoped>
#meeting-card {
  cursor: pointer;
  padding-bottom: 30px;
}

.box-card {
  width: 360px;
  padding-bottom: 0px;
}

.box-card-mobile {
  width: 350px;
  padding-bottom: 0px;
}
.meeting-summary {
  font-size: 0.9em;
}
.attend {
  margin-bottom: 10px;
}

.card-body {
  padding: 8px 15px 15px 15px;
}

.recipe-image {
  width: 100%;
  height: 240px;
  object-fit: cover;
}
.people-attend {
  margin-right: 5px;
}
#meeting-title {
  font-size: 0.8em;
  margin-bottom: 5px;
}
.meeting-text {
  font-size: 0.9em;
  padding-bottom: 5px;
}
.meeting-text-desc {
  font-size: 0.9em;
  padding-bottom: 10px;
}
#meeting-time {
  margin-bottom: 10px;
  font-size: 0.8em;
}
.meeting-tags {
  padding-top: 5px;
}
#meeting-date {
  margin-bottom: 10px;
  font-size: 0.9em;
}
#meeting-date > i {
  margin-right: 8px;
}
#meeting-time > i {
  margin-right: 8px;
}
#meeting-title > i {
  margin-right: 8px;
}

#meeting-link > i {
  margin-right: 8px;
}

#meeting-status {
  font-size: 0.8em;
  font-weight: bold;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}
</style>

<style>
.future-delete {
  font-family: Nunito, Helvetica, Arial, sans-serif;
}
</style>
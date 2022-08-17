<template>
  <div id="settings-bar">
    <div class="page-heading">Settings</div>
    <el-tabs v-model="activeName">
      <el-tab-pane label="General" name="general"> </el-tab-pane>
      <!--<el-tab-pane label="Meeting Types" name="purpose"> </el-tab-pane>-->
      <el-tab-pane style="height: 100%" label="Topics" name="topics">
      </el-tab-pane>
    </el-tabs>

    <div id="setting-card">
      <profile-details v-if="activeName == 'general'" />
      <!--<purpose-setting v-if="activeName == 'purpose'" />-->
    </div>

    <div v-if="activeName == 'topics'" id="topic-parent">
      <div id="topic-list">
        <el-card :body-style="{ height: '80%' }" class="wp-card" shadow="never">
          <div class="page-sub-heading">Topics</div>
          <div>
            <div class="topic-list-item" @click="addTab()">
              <b><i class="el-icon-plus"></i> New recipe</b>
            </div>
            <hr
              style="
                border: 0;
                border-top: 3px solid #eee;
                margin-top: 0px;
                margin-bottom: 0px;
              "
            />
          </div>
          <div
            @click="TopicClicked(topic, index)"
            v-for="(topic, index) in allTopics"
            :key="index"
          >
            <div
              :class="
                index == 0
                  ? 'topic-list-item topic-selected'
                  : 'topic-list-item'
              "
              :id="'topic-item-' + index"
            >
              <span
                :style="
                  'height: 10px; width: 10px; margin-right:8px; background-color:' +
                  topic.meta_data.color +
                  '; border-radius: 50%; display: inline-block;'
                "
              ></span>
              {{ topic.value }}
            </div>
            <hr
              style="
                border: 0;
                border-top: 1px solid #eee;
                margin-top: 0px;
                margin-bottom: 0px;
              "
            />
          </div>
        </el-card>
      </div>

      <div id="topic-info">
        <el-card
          :body-style="{ height: '500px' }"
          class="wp-card"
          shadow="never"
        >
          <div class="page-sub-heading">Feedback</div>

          <!--<topic-keyword-setting
            class="scrollable"
            :TopicObject="allTopics[ActiveTopic]"
            v-on:topicDeleted="TopicDeletedEvent(allTopics[ActiveTopic].id)"
          />-->
        </el-card>
      </div>

      <!-- <div id="topic-setting-list" class="scrollable">
           <el-card class="wp-card" shadow="never">
          <div>
            <div class="topic-list-item" @click="addTab()">
              <b><i class="el-icon-plus"></i> New topic</b>
            </div>
            <hr
              style="
                border: 0;
                border-top: 3px solid #eee;
                margin-top: 0px;
                margin-bottom: 0px;
              "
            />
          </div>
          <div
            @click="TopicClicked(topic, index)"
            v-for="(topic, index) in allTopics"
            :key="index"
          >
            <div
              :class="
                index == 0
                  ? 'topic-list-item topic-selected'
                  : 'topic-list-item'
              "
              :id="'topic-item-' + index"
            >
              <span
                :style="
                  'height: 10px; width: 10px; margin-right:8px; background-color:' +
                  topic.meta_data.color +
                  '; border-radius: 50%; display: inline-block;'
                "
              ></span>
              {{ topic.value }}
            </div>
            <hr
              style="
                border: 0;
                border-top: 1px solid #eee;
                margin-top: 0px;
                margin-bottom: 0px;
              "
            />
          </div>
             </el-card>
        </div>
   
        <div id="topic-setting-content" class="scrollable">
          <topic-keyword-setting
            :TopicObject="allTopics[ActiveTopic]"
            v-on:topicDeleted="TopicDeletedEvent(allTopics[ActiveTopic].id)"
          />
        </div> -->
    </div>
  </div>
</template>
<script>
//import TopicKeywordSetting from "../components/TopicKeywordSetting.vue";
import ProfileDetails from "../components/ProfileDetails.vue";
export default {
  components: {
    //TopicKeywordSetting,
    ProfileDetails,
    //PurposeSetting,
  },
  data() {
    return {
      allTopics: "",
      activeName: "general",
      editableTabsValue: "2",
      tabIndex: 2,
      ActiveTopic: 0,
      TopicsLoaded: false,
    };
  },
  methods: {
    TopicClicked: function (topic, index) {
      var el = document.getElementById("topic-item-" + index);
      var old_el = document.getElementById("topic-item-" + this.ActiveTopic);
      this.ActiveTopic = index;
      if (old_el != null) {
        old_el.classList.remove("topic-selected");
      }

      el.classList.add("topic-selected");
    },
    TopicValueChanged: function (val) {
      var l_id = this.allTopics.find((e) => e.value == val);
      this.$store.dispatch("PatchLabel", { id: l_id.id, value: val });
    },
    addTab() {
      this.$store
        .dispatch("createLabelWithoutParent", {
          value: "New Topic",
          usecase: "TOPIC",
        })
        .then((new_id) => {
          console.log(new_id);
          var new_topic_obj = {
            id: new_id,
            value: "New Topic",
            usecase: "TOPIC",
            children: [],
            meta_data: {},
          };

          new_topic_obj.meta_data.color =
            "#" + Math.floor(Math.random() * 16777215).toString(16);
          new_topic_obj.meta_data.ideal = "0:0";
          // new_topic_obj.meta_data = JSON.stringify(meta_data_obj);
          var meta_data_str = JSON.stringify(new_topic_obj.meta_data);
          this.$store
            .dispatch("PatchTopic", {
              id: new_id,
              content: { meta_data: meta_data_str },
            })
            .then(() => {
              this.allTopics.push(new_topic_obj);
              setTimeout(
                function () {
                  this.TopicClicked(
                    this.allTopics[this.allTopics.length - 1],
                    this.allTopics.length - 1
                  );
                }.bind(this),
                200
              );
            });
        });
    },

    TopicDeletedEvent(id) {
      var obj = this.allTopics.find((el) => el.id == id);
      const index = this.allTopics.indexOf(obj);
      if (index > -1) {
        this.allTopics.splice(index, 1);
        if (index - 1 != -1) {
          this.editableTabsValue = String(this.allTopics[index - 1].id);
          this.TopicClicked(this.allTopics[index - 1], index - 1);
        }
      }
    },
    // handleClose(tag) {
    //   this.analysisTags.splice(this.analysisTags.indexOf(tag), 1);
    // },
  },

  beforeMount() {
    document.title = this.$t('foodrecipe');
    this.$store.dispatch("GetallTopics").then((data) => {
      this.allTopics = data;
      for (var i = 0; i < this.allTopics.length; i++) {
        this.allTopics[i].meta_data = JSON.parse(
          this.allTopics[i].meta_data.replace(/'/g, '"')
        );
      }
      this.editableTabsValue = String(data[0].id);
      this.TopicsLoaded = true;
    });
  },
};
</script>
<style scoped>
#topic-list {
  width: 30%;
}

#topic-info {
  width: 70%;
}
#topicset {
  margin: 20px;
}
#topic-name {
  margin-bottom: 10px;
}
#key-tags {
  margin-bottom: 12px;
  margin-right: 15px;
}
#input-keyword {
  margin-bottom: 20px;
}
#settings-bar {
  position: relative;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.scrollable {
  margin-top: 25px;
  margin-bottom: 10px;
  overflow: scroll;
  max-height: 100%;
}

#topic-parent {
  display: flex;
  flex-direction: row;
  width: 100%;
}

#topic-setting-container {
  font-size: 0.9em;
  height: 100%;
  overflow: hidden;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#topic-setting-container > div {
  padding-top: 20px;
}
.page-sub {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.topic-list-item {
  cursor: pointer;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 15px;
  padding-right: 15px;
}
.topic-selected {
  background: rgb(233, 233, 233);
}

.topic-selected:hover {
  background: rgb(233, 233, 233) !important;
}

.topic-list-item:hover {
  background: rgb(245, 245, 245);
}

.scrollable {
  overflow: scroll;
  max-height: 100%;
}

#topic-setting-list {
  min-width: 200px;
}

#topic-setting-content {
  padding-left: 25px;
  width: 100%;
}
</style>

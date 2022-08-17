<template>
  <div :id="$store.state.isMobile ? 'my-meetings-mobile': 'my-meetings'">
    <div class="page-heading-base">
      <div :class="$store.state.isMobile ? 'page-heading-mobile' :'page-heading'">{{ $t('recipes') }}</div>
      <div id="all-meeting-cta" class="page-heading-cta">
        <div id="search-bar">
          <el-input
            :placeholder="$t('search')"
            prefix-icon="el-icon-search"
            v-model="recipe_search_text"
          >
          </el-input>
          <!--THIS HAS THE KEYUP FOR FUTURE USE ABOVE DOESNT
        <el-input
          placeholder="Search meetings"
          prefix-icon="el-icon-search"
          v-model="meeting_search_text"
          @keyup.native.enter="searchTranscript(meeting_search_text)"
        >
        </el-input>-->
        </div>
        <!--<el-button
          @click="test()"
          type="primary"
          slot="reference"
          ><i class="el-icon-plus el-icon--right"></i> {{ $t('add_new') }}
        </el-button>-->
      </div>
    </div>

    <!--<el-tabs v-model="activeName">
      <el-tab-pane label="My recipes" name="first"></el-tab-pane>
      <el-tab-pane label="All recipes" name="second"></el-tab-pane>
    </el-tabs>-->

    <div :class="$store.state.isMobile ? 'upcoming-meetings-section-mobile' : 'upcoming-meetings-section'">
      <div :class="$store.state.isMobile ? 'upcoming-meeting-cards-mobile' : 'upcoming-meeting-cards'">
        <div
          style="width: 100px; margin: auto; text-align: center"
          v-if="AllRecipes.length == 0 && !isLoadingInProcess"
        >
          <empty />
        </div>
        <div style="text-align: center" v-if="isLoadingInProcess">
          <div class="lds-hourglass"></div>
        </div>
        <div style="text-align: center" v-if="isSearchingTranscripts">
          team of monkeys dispatched to find from recipes
          <div class="lds-hourglass"></div>
        </div>
        <!--<div v-if="filterSearch(TeamMeetings).length == 0">
          Enter to find transcripts with the word: {{ meeting_search_text }}
        </div>-->
        <router-link
          v-for="recipe in filterSearch(AllRecipes)"
          :key="recipe.id"
          :to="openRecipe(recipe)"
        >
          <recipe-card :RecipeObject="recipe" />
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import RecipeCard from "../components/RecipeCard.vue";
//import ImportMeeting from "../components/ImportMeeting.vue";
export default {
  name: "Myrecipes",
  components: {
    RecipeCard,
    //ImportMeeting,
  },
  data() {
    return {
      activeName: "second",
      AllRecipes: [],
      customsearchQuery: [],
      ImportMeetingWindow: false,
      ImportMeetingWindowOld: false,
      isFutureMeetingCardOpen: false,
      FutureMeetingObject: {},
      FutureMeetingEvent: { attendees: {} },
      recipe_search_text: "",
      isLoadingInProcess: true,
      isSearchingTranscripts: false,
      isTranscriptSearch: false,
      transcriptKey: "",
      transcriptPreviews: [],
      drawer: false,
      advancedSearch: [],
      searchStrings: {
        title: "",
        transcript: "",
        company: "",
        date: "",
        purpose: "",
        topics: "",
        score: "",
        participants: "",
      },
    };
  },
  methods: {
    updateTerms(data) {
      this.advancedSearch.push(data);
      this.searchStrings[data.search] +=
        data.operation + ":" + data.value + ";";
      // force filter
      this.searchTranscript(this.searchStrings);
    },
    filterSearch(Meetings) {
      var results = this.recipe_search_text
        ? Meetings.filter(this.createFilter(this.recipe_search_text))
        : Meetings;
      return results;
    },
    createFilter(queryString) {
      return (recipe) => {
        return (
          recipe.name.toLowerCase().includes(queryString.toLowerCase()) ||
          recipe.tags.toLowerCase().includes(queryString.toLowerCase())
        );
      };
    },
    test() {
      console.log("called");
      console.log(this.recipe_search_text);
    },
    openRecipe(meeting) {
      return "recipes/" + meeting.id;
    },
  },
  beforeMount() {
    document.title = this.$t('foodrecipe');
    this.$store.dispatch("GetRecipes").then((data) => {
      this.AllRecipes = data;
      this.isLoadingInProcess = false;
    });
  },
};
</script>
<style scoped>
#my-meetings {
  display: flex;
  margin-top: 50px;
  flex-direction: column;
}
#my-meetings-mobile {
  display: flex;
  margin-top: 0px;
  flex-direction: column;
}

.upcoming-meetings-section {
  display: flex;
  margin-right: -30px;
}

.upcoming-meetings-section-mobile {
  display: flex;
  padding-bottom: 100px;
}
.upcoming-meeting-cards {
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
  margin-bottom: 15px;
  justify-content: center;
}

.upcoming-meeting-cards-mobile {
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -moz-flex;
  display: -webkit-flex;
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  margin-bottom: 30px;
  justify-content: center;
}

.mobile {
  justify-content:center;
}
#all-meeting-cta {
  width: 60%;
  margin-right:15%
}
#all-meeting-cta > div {
  margin-right: 20px;
}
#search-bar {
  width: 100%;;
}
.upcoming-meeting-cards > * {
  margin-right: 30px;
}
#meetings-sub-menu {
  margin-left: auto;
  width: fit-content;
  display: flex;
  flex-direction: row;
}
#score-card {
  height: 500px;
}
.lds-hourglass {
  position: absolute;
  left: 50%;
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
@keyframes lds-hourglass {
  0% {
    transform: rotate(0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  50% {
    transform: rotate(900deg);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  100% {
    transform: rotate(1800deg);
  }
}
.scrollable {
  margin-bottom: 10px;
  max-height: 100%;
}
</style>
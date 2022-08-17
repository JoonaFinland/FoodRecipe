<template>
  <div>
    HELLO WORLD
  </div>
</template>
<script>
//import RecipeCard from "../components/RecipeCard.vue";
//import ImportMeeting from "../components/ImportMeeting.vue";
export default {
  name: "Myrecipes",
  components: {
    //RecipeCard,
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
  flex-direction: column;
  height: 100%;
}
.upcoming-meetings-section {
  display: flex;
  height: 100%;
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
}
#all-meeting-cta {
  width: 70%;
}
#all-meeting-cta > div {
  margin-right: 20px;
}
#search-bar {
  width: 100%;;
}
.upcoming-meeting-cards > * {
  margin-right: 30px;
  margin-bottom: 30px;
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
  margin-top: 25px;
  margin-bottom: 10px;
  overflow: scroll;
  max-height: 100%;
}
</style>
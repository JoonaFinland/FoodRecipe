<template>
  <div id="recipe" v-if="!isLoading">
    MOBILE
    <div id="name_info" class="recipe-inner">
      <div class="recipe-title">
        {{ RecipeObject.name }}
      </div>
    </div>
    <div id="tags" class="recipe-inner">
      <el-tag
        v-for="tag in getTags()"
        :key="tag"
        class="tag"
        type="info"
        effect="dark"
        size="small"
      >
        {{tag}}
      </el-tag>
    </div>
    <div id="time_portions" class="recipe-inner">
      <div class="time_portions_inner">
        <i class="el-icon-time"> </i> {{ getTotalTime() }} {{ $t('minutes') }}
      </div>
      <div class="time_portions_inner">
        <i class="el-icon-user"> </i> {{ getPortions() }} {{ $t('portions') }}
      </div>
    </div>
    <div id="thumbnail" class="recipe-inner">
      <img :src="RecipeObject.img" :alt="RecipeObject.name" class="recipe-image">
    </div>

    <!--<div id="name_info" class="recipe-inner" >
      <div class="recipe-description">
        {{ RecipeObject.details }}
      </div>
    </div>-->
    <div class="food" v-for="(food,ind) in RecipeObject.foods" :key="food.name">
      <h2 class="food-title">{{ food.name }}</h2>
      <el-row :gutter="50">
        <el-col :span="12">
          <div id="ingredients">
            <h3>{{ $t('ingredients') }}</h3>
            <div class="ing_row" v-for="(data,row) in getIngredients(ind)" :key="data.item">
              <el-row :gutter="40">
                <el-col :span="6">
                  <div style="text-align: right">
                    {{ data.amount }}
                  </div>
                </el-col>
                <el-col :span="18">
                  <div>
                    {{ data.name }}
                  </div>
                </el-col>
              </el-row>
              <div v-if="row != getIngredients(ind).length - 1" class="custom_divider">
                <!---->
              </div>
            </div>
          </div>
        </el-col>
        <el-col :span="12">
          <div id="instructions">
            <h3>{{ $t('instructions') }}</h3>
            <!--{{ getInstructions(ind) }}-->
            <div class="instruction-step" v-for="(step,num) in getInstructions(ind)" :key="num">
              <p>{{ num+1 }}. {{ step }}</p>
            </div>
          </div>
        </el-col>
      </el-row>
      <div v-if="ind != RecipeObject.foods.length - 1" class="custom_divider thick-divider">
        <!---->
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "RecipePage",
  components: {
  },
  data() {
    return {
      RecipeObject: {},
      isLoading: true,
    };
  },
  methods: {
    getTags() {
      let tags = this.RecipeObject.tags.split(",");
      if (tags[0] == '') {
        return []
      }
      return tags;
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
    },
    getIngredients(ind) {
      var output = []
      this.RecipeObject.foods[ind].ingredients.forEach(ingredient => {
        let obj = {
          amount: parseFloat(ingredient.quantity)+' '+ingredient.ingredient.unit,
          name: ingredient.ingredient.name
        }
        output.push(obj);
      })
      return output
    },
    getInstructions(ind) {
      const steps = this.RecipeObject.foods[ind].instructions.split("|");
      return steps;
    },
  },
  beforeMount() {
    this.$store.dispatch("GetRecipeByID", this.$route.params.id)
    .then(response => {
      console.log(response)
      this.RecipeObject = response;
      this.isLoading = false;
    })
  }
};
</script>
<style scoped>
.recipe-image {
  width: 100%;
  border-radius: 15px;
  /*clip-path: polygon(0 10%, 100% 10%, 100% 90%, 0% 90%);*/
  height: 850px;
  object-fit: cover;
}
#time_portions {
  display: flex;
}
.time_portions_inner {
  padding-right: 25px;
}
.food-title {
  margin-bottom: 0px;
}
.instruction-step {
  width: 100%;
  word-wrap: break-word;
}
.break {
  width: 100%;
  word-wrap: break-word;
}
.thick-divider {
  height: 3px !important;
}
.custom_divider {
  display: block;
  height: 1px;
  width: 100%;
  background-color: #DCDFE6;
  position: relative;
  margin: 10px 0px 10px 0px;
}

.ing_row {
  margin-top: 0px;
  margin-bottom: 0px;
}
.recipe-title {
  font-weight: bold;
  font-size: 1.6em;
}

.tag {
  margin-right: 8px;
}

#name_info {
  margin-top: 15px;
}

.recipe-inner {
  margin-bottom: 10px;
}

#recipe {
  margin-left: 15%;
  margin-right: 15%;
  margin-bottom: 150px;
}
</style>

<template>
  <div id="recipe" :class="$store.state.isMobile ? 'recipe-mobile' : 'recipe-desktop'" v-if="!isLoading">
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
      <!--<div class="time_portions_inner">
        <i class="el-icon-time"> </i> {{ getTotalTime() }} {{ $t('minutes') }}
      </div>-->
      <div class="time_portions_inner">
        <i class="el-icon-user"> </i> {{ getPortions() }} {{ $t('portions') }}
      </div>
    </div>
    <div id="thumbnail" class="recipe-inner">
      <img :src="RecipeObject.img" :alt="RecipeObject.name" :class="$store.state.isMobile ? 'recipe-image-mobile' : 'recipe-image-desktop'">
    </div>

    <!--<div id="name_info" class="recipe-inner" >
      <div class="recipe-description">
        {{ RecipeObject.details }}
      </div>
    </div>-->
    <div class="food" v-for="(food,ind) in RecipeObject.foods" :key="food.name">
      <h2 class="food-title">{{ food.name }}</h2>
      <el-row :gutter="getGutter()" class="flex-parent">
        <el-col :span="12" class="flex-child">
          <!--<div id="ingredients" >
            <h3>{{ $t('ingredients') }}</h3>
            <div class="ing_row" v-for="(data,row) in getIngredients(ind)" :key="data.item">
              <el-row :gutter="getGutter2()">
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
              <div v-if="row != getIngredients(ind).length - 1" :class="$store.state.isMobile ? 'custom_divider-mobile' : 'custom_divider'">
                
              </div>
            </div>
            
          </div>-->
          <div id="ingredients" v-for="data in getIngredients_temp(ind)" :key="data.item">
            <h3>{{ data.name }}</h3>
            <div class="ing_row" v-for="(ing,row) in data.ings" :key="ing.right">
              <el-row :gutter="getGutter2()">
                <el-col :span="6">
                  <div style="text-align: right">
                    {{ ing.left }}
                  </div>
                </el-col>
                <el-col :span="18">
                  <div>
                    {{ ing.right }}
                  </div>
                </el-col>
              </el-row>
              <div v-if="row != getIngredients(ind).length - 1" :class="$store.state.isMobile ? 'custom_divider-mobile' : 'custom_divider'">
                
              </div>
            </div>
            
          </div>
        </el-col>
        <el-col :span="12" class="flex-child">
          <div id="instructions">
            <h3>{{ $t('instructions') }}</h3>
            <!--{{ getInstructions(ind) }}-->
            <div class="instruction-step" v-for="(step,num) in getInstructions(ind)" :key="num">
              <p><b>{{ num+1 }}.</b> {{ step }}</p>
            </div>
          </div>
        </el-col>
      </el-row>
      <div id="hints" v-if="RecipeObject.foods[ind].hints != ''" style="text-align: center !important;">
        <h3>{{ $t('hints') }}</h3>
        <!--{{ getInstructions(ind) }}-->
        <div class="instruction-step" v-for="(step,num) in getHints(ind)" :key="num">
          <p>{{ step }}</p>
          <el-divider v-if="num != getHints(ind).length - 1">
            <i class="el-icon-star-on"></i>
          </el-divider>
        </div>
      </div>
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
    getGutter() {
      return this.$store.state.isMobile ? 5 : 30;
    },
    getGutter2() {
      return this.$store.state.isMobile ? 10 : 40;
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
    convertIng(str) {
      let list = []
        str.split('|').forEach(ing_raw => {
        let left = ing_raw.split('+')[0]
        if (left === '') {
          left = ' ';
        }
        let obj = {
          left: left,
          right: ing_raw.split('+')[1]
        }
        list.push(obj)
      })
      return list
    },
    getIngredients_temp(ind) {
      var output = []
      JSON.parse(this.RecipeObject.foods[ind].ingredients_temp).forEach(ingredient => {
        let obj = {
          name: ingredient.name,
          ings: this.convertIng(ingredient.ings)
        }
        output.push(obj)
      })
      /*this.RecipeObject.foods[ind].ingredients.forEach(ingredient => {
        let obj = {
          amount: parseFloat(ingredient.quantity)+' '+ingredient.ingredient.unit,
          name: ingredient.ingredient.name
        }
        output.push(obj);
      })*/
      console.log('**********')
      console.log(output)
      return output
    },
    getInstructions(ind) {
      const steps = this.RecipeObject.foods[ind].instructions.split("|");
      return steps;
    },
    getHints(ind) {
      const steps = this.RecipeObject.foods[ind].hints.split("|");
      return steps;
    }
  },
  beforeMount() {
    this.$store.dispatch("GetRecipeByID", this.$route.params.id)
    .then(response => {
      console.log(response)
      this.RecipeObject = response;
      this.isLoading = false;
      document.title = this.RecipeObject.name;
    })
  }
};
</script>
<style scoped>

.flex-parent {
  display: flex !important;
  flex-direction: row;
}

.flex-child {
  flex: 1;
}

.recipe-image-mobile {
  width: 100%;
  border-radius: 15px;
  /*clip-path: polygon(0 10%, 100% 10%, 100% 90%, 0% 90%);*/
  height: 300px;
  object-fit: cover;
}

.el-divider__text {
  background-color: #dee9eb !important;
  padding: 0 10px !important; 
}

.recipe-image-desktop {
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

.custom_divider-mobile {
  display: block;
  height: 1px;
  width: 95%;
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

.recipe-desktop {
  margin-left: 15%;
  margin-right: 15%;
  margin-bottom: 150px;
}
.recipe-mobile {
  margin-left: 5px;
  margin-right: 5px;
  margin-bottom: 150px;
}
</style>

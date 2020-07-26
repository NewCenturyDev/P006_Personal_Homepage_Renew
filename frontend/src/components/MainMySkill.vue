<template>
  <div class="mainMySkill" id="skill">
    <div class="title">My Skills</div>
    <div class="myPresentationContainer">
      <el-card class="skillList"
        v-for="(skillCategory, skillCategoryIndex) in $store.state.skillCategory"
        :style="{ backgroundColor: getBackgroundColor(skillCategoryIndex) }"
        :key="skillCategoryIndex">
        <div class="skillTitle">{{ skillCategory.category }}</div>
        <div class="skillContainer">
          <div class="skill"
            v-for="(skill, skillIndex) in $store.getters.getSkillByCategory(skillCategory.category)"
            :key="skillIndex">
            <img class="skillImage" :src="skill.image" />
            <div class="skillName">{{ skill.name }}</div>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainMySkill',
  methods: {
    getBackgroundColor(index) {
      const colorList = ['rgba(236, 056, 067, 0.7)', 'rgba(247, 193, 000, 0.7)', 'rgba(140, 124, 091, 0.7)', 'rgba(178, 209, 053, 0.7)', 'rgba(000, 186, 201, 0.7)', 'rgba(124, 089, 119, 0.7)', ];
      return colorList[index % 6];
    }
  },
}
</script>

<style lang="scss" scoped>
.mainMySkill {
  max-width: 1500px;
  padding: 50px calc(50% - 600px);
  background-color: #ffffff;
  .title {
    width: 100%;
    height: 50px;
    margin-bottom: 50px;
    font-size: 40px;
    line-height: 50px;
    text-align: center;
  }
  .myPresentationContainer {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1500px;
    background-color: #ffffff;
    .skillList {
      width: 350px;
      height: 500px;
      margin: 0 15px; 
      margin-bottom: 15px;
      .skillTitle {
        color: #ffffff;
        font-size: 28px;
        line-height: 35px;
      }
      .skillContainer {
        .skill {
          width: 310px;
          height: 60px;
          .skillImage {
            float: left;
            width: 50px;
            height: 50px;
            margin: 5px;
            border-radius: 5px;
            background-color: #ffffff;
          }
          .skillName {
            float: right;
            width: 220px;
            height: 60px;
            margin: 0 15px;
            font-size: 18px;
            text-align: left;
            color: #ffffff;
            line-height: 60px;
          }
        }
      }
    }
  }
}
</style>

<template>
  <div class="mainProjects" id="projects">
    <div class="title">My Projects</div>
    <div class="myProjectContainer">
      <el-tabs v-model="activeTab">
        <el-tab-pane
          v-for="(projectCategory, categoryIndex) in $store.state.projectCategory"
          :key="categoryIndex"
          :name="projectCategory.category"
          :label="projectCategory.category">
            <div class="cardContainer"
              v-for="(project, projectIndex) in $store.getters.getProjectByCategory(projectCategory.category)"
              :key="projectIndex">
              <el-card shadow="hover" body-style="{ width: calc(100% - 50px); padding: 0; }">
                <div class="projectList">
                  <div class="projectImageContainer">
                    <img class="projectImage" :src="`../assets/projects/${project.screenshot[0]}`" />
                    <div class="projectBtnContainer">
                      <el-button class="projectBtn" type="plane" v-on:click="openGithub(project.link)">
                        Github 열기
                      </el-button>
                      <el-button class="projectBtn" type="plane" v-on:click="gotoDetail(project.id)">
                        자세히 보기
                      </el-button>
                    </div>
                  </div>
                  <div class="projectInfo">
                    <div class="projectTitle">{{ project.name }}</div>
                    <div class="projectDiscription" v-html="project.discription"></div>
                    <div class="projectStackContainer">
                      <div class="projectStack"
                        v-for="(stack, stackIndex) in project.stackTags"
                        :key="stackIndex">
                        {{ stack }}
                      </div>
                    </div>
                  </div>
                </div>
              </el-card>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainProjects',
  data() {
    return {
      activeTab: 'Web',
    };
  },
  methods: {
    openGithub(link) {
      window.open(link);
    },
    gotoDetail(projectID) {
      this.$router.push({
        name: 'Project',
        query: { id: projectID },
      });
    },
  }
}
</script>

<style lang="scss">
/* UI library override */
.mainProjects {
  .el-tabs__header {
    width: calc(100% - 50px) !important;
    margin: 0 25px !important;
  }
  .el-tabs__content {
    width: calc(100% - 50px) !important;
    margin: 0 25px !important;
  }
  .el-tabs__header is-top {
    margin: 0 !important;
  }
  .el-card {
    border-radius: 0px !important;
  }
  .el-button {
    border-left: 0 !important;
    border-right: 0 !important;
    border-top: 0 !important;
    border-bottom: 1px solid #ebeef5;
    border-radius: 0px !important;
  }
  .el-button+.el-button {
    margin: 0 !important;
  }
}
</style>

<style lang="scss" scoped>
.mainProjects {
  max-width: 1500px;
  padding: 50px calc(50% - 600px);
  background-color: #f0f8ff;
  .title {
    width: 100%;
    height: 50px;
    margin-bottom: 50px;
    font-size: 40px;
    line-height: 50px;
    text-align: center;
  }
  .myProjectContainer {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1200px;
    .cardContainer {
      margin: 15px 0;
      .projectList {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        width: 100%;
        .projectImageContainer {
          display: flex;
          flex-direction: column;
          flex-wrap: wrap;
          width: 310px;
          .projectImage {
            width: 310px;
            height: 200px;
          }
          .projectBtnContainer {
            width: 310px;
            display: flex;
            flex-direction: column;
            flex-wrap: wrap;
            justify-content: right;
            max-height: 180px;
            .projectBtn {
              width: 100%;
            }
          }
        }
        .projectInfo {
          min-width: 260px;
          max-width: 600px;
          margin: 10px 25px;
          .projectTitle {
            width: 100%;
            margin: 5px 0;
            text-align: left;
            font-size: 28px;
            line-height: 35px;
          }
          .projectDiscription {
            width: 100%;
            margin: 15px 0;
            text-align: left;
            font-size: 15px;
            line-height: 20px;
          }
          .projectStackContainer {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            width: 100%;
            text-align: left;
            font-size: 12px;
            color: #bbbbbb;
            line-height: 15px;
            .projectStack {
              margin-right: 10px;
            }
          }
        }
      }
    }
  }
}
</style>

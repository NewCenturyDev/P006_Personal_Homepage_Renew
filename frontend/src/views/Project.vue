<template>
  <div class="project">
    <el-page-header class="header" @back="goHome" title="Home" :content="project.name"></el-page-header>
    <el-divider></el-divider>
    <div class="contents">
      <el-card class="contentCard" shadow="hover" :body-style="{ padding: 0 }">
        <el-carousel height="500px">
          <el-carousel-item
            v-for="(screenshot, screenshotIndex) in project.screenshot"
            :key="screenshotIndex">
              <img class="contentImage" :src="require(`../assets/projects/${screenshot}`)"/>
          </el-carousel-item>
        </el-carousel>
      </el-card>
      <el-card class="contentCard" shadow="hover">
        <el-header class="contentTitle">{{ project.name }}</el-header>
        <el-divider content-position="left">Project Document</el-divider>
        <el-main class="contentText">
          <v-md-editor mode="preview" v-model="project.content"></v-md-editor>
        </el-main>
      </el-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Project',
  data() {
    return {
      project: this.$store.state.projects.find((project) => (project.id === Number(this.$route.query.id))),
    };
  },
  methods: {
    goHome() {
      this.$router.push('/');
    },
    openGithub(link) {
      window.open(link);
    },
  }
}
</script>

<style lang="scss">
/* UI Library CSS Override */
.v-md-editor-preview {
  padding: 0 !important;
  padding-bottom: 25px !important;
}
</style>

<style lang="scss" scoped>
.project {
  .header {
    height: 50px;
    padding: 0 25px;
    line-height: 50px;
  }
  .contents {
    max-width: 1200px;
    margin: 0 auto;
    .contentCard {
      width: calc(100% - 50px);
      margin: 25px;
      .contentImage {
        width: 100%;
        height: 100%;
      }
      .contentTitle {
        font-size: 25px;
        font-weight: bold;
        line-height: 60px;
      }
      .contentText {
        padding: 0;
      }
    }
  }
}
</style>

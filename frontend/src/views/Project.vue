<template>
  <div class="project">
    <el-page-header class="header" @back="goHome" title="Home" :content="$route.params.project.name"></el-page-header>
    <el-divider></el-divider>
    <div class="contents">
      <el-card class="contentCard" shadow="hover">
        <el-carousel height="500px">
          <el-carousel-item
            v-for="(screenshot, screenshotIndex) in $route.params.project.screenshot"
            :key="screenshotIndex">
              <img :src="require(`../assets/projects/${screenshot}`)"/>
          </el-carousel-item>
        </el-carousel>
      </el-card>
      <el-card class="contentCard" shadow="hover">
        <el-header>프로젝트 개요</el-header>
        <el-button @click="openGithub($route.params.project.link)">Github</el-button>
        <el-main>{{ $route.params.project.discription }}</el-main>
      </el-card>
      <el-card class="contentCard" shadow="hover">
        <el-header>프로젝트 기술 스택</el-header>
        <el-main>{{ $route.params.project.stack }}</el-main>
      </el-card>
      <el-card class="contentCard" shadow="hover">
        <el-header>프로젝트 기획</el-header>
        <el-main>{{ $route.params.project.concept }}</el-main>
      </el-card>
      <el-card class="contentCard" shadow="hover">
        <el-header>프로젝트 기술문서</el-header>
        <el-main>{{ $route.params.project.document }}</el-main>
      </el-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Project',
  props: {
    project: Object,
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
  }
  .contentCard {
    width: calc(100% - 50px);
    margin: 25px;
  }
}
</style>

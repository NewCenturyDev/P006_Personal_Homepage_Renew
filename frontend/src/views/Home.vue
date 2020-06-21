<template>
  <div class="home">
    <MainBackground/>
    <MainProfile/>
    <el-divider></el-divider>
    <MainMySkill/>
    <el-divider></el-divider>
    <MainProjects/>
    <el-divider></el-divider>
    <MainContact/>
  </div>
</template>

<script>
// @ is an alias to /src
import MainBackground from '@/components/MainBackground.vue';
import MainProfile from '@/components/MainProfile.vue';
import MainMySkill from '@/components/MainMySkill.vue';
import MainProjects from '@/components/MainProjects.vue';
import MainContact from '@/components/MainContact.vue';

export default {
  name: 'Home',
  components: {
    MainBackground, MainProfile, MainMySkill, MainProjects, MainContact,
  }
}
</script>

<style lang="scss">
/* UI Library Override */
.el-divider--horizontal {
  margin: 0 !important;
}
.el-divider {
  background-color: #cbced5 !important;
}
</style>

<template>
  <div class="login">
    <el-card class="loginForm">
      <el-header class="loginTitle">포트폴리오 관리</el-header>
      <el-input class="loginBtn" placeholder="ID" v-model="input.id"></el-input>
      <el-input class="loginBtn" placeholder="PW" v-model="input.pw" show-password></el-input>
      <el-button class="loginBtn">Login</el-button>    
    </el-card>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Login',
  data() {
    return {
      input: {
        id: '',
        pw: '',
      },
    };
  },
}
</script>

<style lang="scss" scoped>
.login {
  .loginForm {
    max-width: 500px;
    height: 300px;
    margin: 100px auto;
    .loginTitle {
      font-size: 30px;
      line-height: 50px;
    }
  }
}
</style>

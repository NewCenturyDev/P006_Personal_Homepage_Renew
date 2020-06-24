<template>
  <div class="loginModal">
    <el-dialog class="loginForm" :visible.sync="$parent.dialogVisible">
      <el-header class="loginTitle">포트폴리오 관리</el-header>
      <el-input class="loginInput" placeholder="ID" v-model="input.id"></el-input>
      <el-input class="loginInput" placeholder="PW" v-model="input.pw" show-password></el-input>
      <el-button class="loginBtn" type="primary">Login</el-button>
    </el-dialog>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'LoginModal',
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

<style lang="scss">
/* UI Library CSS Override */
.loginModal {
  .el-dialog {
    width: 100% !important;
    margin: 0 !important;
    .el-dialog__header {
      padding: 0 !important;
    }
  }
}
</style>

<style lang="scss" scoped>
.loginModal {
  .loginForm {
    max-width: 500px;
    height: 300px;
    margin: 100px auto;
    .loginTitle {
      font-size: 30px;
      line-height: 50px;
    }
    .loginInput {
      width: 80%;
      margin: 10px auto;
    }
    .loginBtn {
      width: 30%;
      margin: 10px auto;
    }
  }
}
</style>

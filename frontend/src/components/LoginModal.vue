<template>
  <div class="loginModal">
    <el-dialog class="loginForm" :visible.sync="$parent.dialogVisible">
      <el-header class="loginTitle">포트폴리오 관리</el-header>
      <el-input class="loginInput" placeholder="ID" v-model="input.username"></el-input>
      <el-input class="loginInput" v-on:keyup.enter="login" placeholder="PW" v-model="input.password" show-password></el-input>
      <el-button class="loginBtn" v-on:click="login" type="primary">Login</el-button>
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
        username: '',
        password: '',
      },
    };
  },
  async beforeMount() {
    try {
      const isLoggedIn = await this.$store.dispatch('checkSession');
      if (isLoggedIn === true) {
        this.$parent.dialogVisible = false;
      }
    } catch (error) {
      alert(error);
    }
  },
  methods: {
    async login() {
      try {
        await this.$store.dispatch('login', this.input);
        this.$parent.dialogVisible = false;
        this.$router.push('/admin');
      } catch (error) {
        alert(error);
        this.$parent.dialogVisible = false;
      } finally {
        this.input = {
          username: '',
          password: '',
        };
      }
    }
  }
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

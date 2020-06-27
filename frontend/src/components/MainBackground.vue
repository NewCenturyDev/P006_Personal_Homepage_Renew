<template>
  <div class="mainBackground" :style="{ height: `${imageHeight}px` }">
    <LoginModal :dialogVisible="dialogVisible" />
    <div class="header" v-if="dynamicStyle === 'greetingsContainer'">
      <div class="headerBtn" v-scroll-to="'#profile'">Profile</div>
      <div class="headerBtn" v-scroll-to="'#skill'">Skill</div>
      <div class="headerBtn" v-scroll-to="'#projects'">Projects</div>
      <div class="headerBtn" v-scroll-to="'#contact'">Contact</div>
      <div>
        <el-button v-if="sessionCheck === true" class="loginBtn" type="primary" disable v-on:click="gotoAdmin">
          Admin
        </el-button>
        <el-button v-else class="loginBtn" type="primary" disable v-on:click="gotoLogin">
          Login
        </el-button>
      </div>
    </div>
    <div :class="dynamicStyle" :style="{ paddingTop: `${imageHeight / 2 - 120}px` }">
      <div class="greetingsMain">Web developer aspirant, <br/> SeongMin Yun</div>
      <div class="greetingsSub">웹 개발자를 꿈꾸는 컴퓨터공학도, 윤성민입니다</div>
    </div>
    <img class="arrowDown" src="@/assets/arrowDown.png" />
  </div>
</template>

<script>
// @ is an alias to /src
import LoginModal from '@/components/LoginModal.vue';

export default {
  name: 'MainBackground',
  components: {
    LoginModal,
  },
  data() {
    return {
      dialogVisible: false,
      sessionCheck: false,
      dynamicStyle: window.innerWidth >= 500 ? 'greetingsContainer' : 'mobile-greetingsContainer',
      imageHeight: window.innerHeight,
    };
  },
  async beforeMount() {
    try {
      await this.$store.dispatch('checkSession');
      this.sessionCheck = true;
    } catch (error) {
      if (error === '로그인 해주세요') {
        this.sessionCheck = false;
      } else {
        this.sessionCheck = false;
        alert(error);
      }
    }
    if (window.innerWidth >= 500) {
      window.addEventListener('resize', () => {
        this.imageHeight = window.innerHeight;
      });
    }
  },
  beforeDestroy() {
    if (window.innerWidth >= 500) {
      window.removeEventListener('resize', () => {});
    }
  },
  methods: {
    gotoLogin() {
      this.dialogVisible = true;
    },
    gotoAdmin() {
      this.$router.push('/admin');
    },
  }
}
</script>

<style lang="scss" scoped>
.mainBackground {
  position: relative;
  width: 100%;
  background-image: url('../assets/main.jpeg');
  background-size: cover;
  .header {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-end;
    width: calc(100% - 20px);
    padding: 10px;
    .headerBtn {
      width: 100px;
      height: 40px;
      color: #ffffff;
      line-height: 40px;
      font-size: 15px;
      cursor: pointer;
    }
  }
  .greetingsContainer {
    margin: 0 auto;
    max-width: 500px;
    height: 150px;
    text-align: center;
    color: #ffffff;
    .greetingsMain {
      font-size: 45px;
      line-height: 60px;
    }
    .greetingsSub {
      margin-top: 20px;
      font-size: 20px;
    }
  }
  .mobile-greetingsContainer {
    margin: 0 auto;
    max-width: 300px;
    height: 100px;
    text-align: center;
    color: #ffffff;
    .greetingsMain {
      font-size: 30px;
      line-height: 40px;
    }
    .greetingsSub {
      margin-top: 15px;
      font-size: 15px;
    }
  }
  .arrowDown {
    position: absolute;
    bottom: 0;
    left: calc(50% - 25px);
    width: 50px;
    height: 50px;
    margin-bottom: 10px;
    animation: updown 2.5s infinite;
    @keyframes updown {
      0% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
      100% { transform: translateY(0); }
    }
  }
}
</style>

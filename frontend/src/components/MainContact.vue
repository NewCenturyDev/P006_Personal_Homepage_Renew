<template>
  <div class="mainContact" id="contact">
    <div class="title">Contact</div>
    <div class="contactBtnContainer">
      <el-button class="contactBtn" type="primary" v-on:click="openLink('https://github.com/HyperTech99')">
        Github
      </el-button>
      <el-button class="contactBtn" type="primary" v-on:click="openLink('https://www.rocketpunch.com/@smyun99')">
        로켓펀치
      </el-button>
      <el-button class="contactBtn" type="primary" v-on:click="openLink('https://www.facebook.com/profile.php?id=100005977243915')">
        FaceBook
      </el-button>
      <el-button class="contactBtn" type="primary" v-on:click="openMail('mailto:smyun99@gmail.com')">
        E-Mail
      </el-button>
      <el-button class="contactBtn" type="primary" disabled v-on:click="openMail('')">
        휴대전화
      </el-button>
      <el-button class="contactBtn" type="primary" disabled v-on:click="openLink('')">
        이력서 (PDF)
      </el-button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainContact',
  methods: {
    openLink(url) {
      window.open(url);
    },
    openMail(address) {
      parent.location.href = address;
    }
  }
}
</script>

<style lang="scss" scoped>
.mainContact {
  max-width: 1500px;
  padding: 50px calc(50% - 600px);
  background-color: #483d8b;
  .title {
    width: 100%;
    height: 50px;
    margin-bottom: 50px;
    font-size: 40px;
    line-height: 50px;
    text-align: center;
    color: #ffffff;
  }
  .contactBtnContainer {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    .contactBtn {
      width: 150px;
      height: 40px;
      margin: 10px;
    }
  }
}
</style>

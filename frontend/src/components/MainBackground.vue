<template>
  <div class="mainBackground" :style="{ height: `${imageHeight}px` }">
    <div :class="dynamicStyle" :style="{ paddingTop: `${imageHeight / 2 - 75}px` }">
      <div class="greetingsMain">Web developer aspirant, <br/> SeongMin Yun</div>
      <div class="greetingsSub">웹 개발자를 꿈꾸는 컴퓨터공학도, 윤성민입니다</div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainBackground',
  data() {
    return {
      dynamicStyle: window.innerWidth >= 500 ? 'greetingsContainer' : 'mobile-greetingsContainer',
      imageHeight: window.innerHeight,
    };
  },
  beforeMount() {
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
  }
}
</script>

<style lang="scss" scoped>
.mainBackground {
  width: 100%;
  background-image: url('../assets/main.jpeg');
  background-size: cover;
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
}
</style>

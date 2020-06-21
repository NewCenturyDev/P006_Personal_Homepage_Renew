<template>
  <div class="mainProfile">
    <div class="myPhotoContainer">
      <img class="myPhoto" width="350px" height="350px" src="@/assets/myPhoto.jpg" />
      <div class="name">윤성민</div>
      <el-button class="github" type="primary" v-on:click="openGithub">
        {{ codename }}
      </el-button>
      <div class="presentation" v-html="presentation"></div>
    </div>
    <div class="myHistoryContainer">
      <div class="myHistoryTitle">My History</div>
      <div class="myHistory">
        <el-timeline>
          <el-timeline-item
            v-for="(activity, activityIndex) in activities"
            :key="activityIndex"
            :timestamp="activity.timestamp">
            {{activity.content}}
          </el-timeline-item>
        </el-timeline>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainProfile',
  data() {
    return {
      codename: '(GitHub) HyperTech99 | Debugging BattleCruiser',
      presentation: '열정적으로 배우는 신입 개발자 지망생입니다.<br/>보기 좋은 음식이 먹기도 좋은 법인 것처럼, 상세한 명세와 문서, 명료한 주석, 클린 코딩을 지향합니다.<br/>“1일 1개발”, “구글링의 생활화”, “StackOverFlow에 답이 있다”를 인생의 모토로 삼고 있습니다.',
      activities: [
        {
          content: '저현자율형공립고등학교 졸업',
          timestamp: '2018. 02.',
        },
        {
          content: '세종대학교 컴퓨터공학과 입학',
          timestamp: '2018. 03.',
        },
        {
          content: '세종대학교 2018 알고리즘 경진대회 장려상 수상',
          timestamp: '2018. 09.',
        },
        {
          content: '세종대학교 웹개발 동아리 OpenYearRound 7기',
          timestamp: '2019. 04.',
        },
        {
          content: '세종대학교 2019 알고리즘 경진대회 3등상 수상',
          timestamp: '2019. 09.',
        },
        {
          content: '세종대학교 제 7회 SW. 인공지능 해커톤 은상 수상',
          timestamp: '2019. 12.',
        },
        {
          content: 'PiLab 스타트업 병역특례(보충역) 입사',
          timestamp: '2020. 01.',
        },
        {
          content: '세종대학교 컴퓨터공학과 2학년 수료 (휴학)',
          timestamp: '2020. 02.',
        },
        {
          content: '병역특례개발자(보충역 산업기능요원) 편입',
          timestamp: '2020. 03.',
        },
      ],
    };
  },
  methods: {
    openGithub() {
      window.open('https://github.com/HyperTech99');
    },
  },
}
</script>

<style lang="scss" scoped>
.mainProfile {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  max-width: 1000px;
  padding: 50px calc(50% - 500px);
  padding-top: 100px;
  background-color: #eeeeee;
  .title {
    width: 100%;
    height: 50px;
    margin-bottom: 50px;
    font-size: 40px;
    line-height: 50px;
    text-align: left;
  }
  .myPhotoContainer {
    width: 500px;
    height: 700px;
    .myPhoto {
      width: 350px;
      height: 350px;
      margin: 10px auto;
    }
    .name {
      width: 100%;
      height: 50px;
      font-size: 28px;
      line-height: 50px;
      text-align: center;
    }
    .presentation {
      width: 350px;
      margin: 30px auto;
      font-size: 15px;
      line-height: 20px;
      text-align: left;
    }
  }
  .myHistoryContainer {
    width: 500px;
    height: 700px;
    .myHistoryTitle {
      width: 100%;
      height: 50px;
      font-size: 35px;
      line-height: 50px;
    }
    .myHistory {
      width: 100%;
      margin: 25px auto;
      height: 600px;
      font-size: 15px;
      line-height: 25px;
      overflow-y: auto;
      .timestampContainer {
        float: left;
        width: calc(25% - 11px);
        height: 400px;
        padding-right: 10px;
        border-right: 1px solid #000000;
        text-align: right;
      }
      .historyContainer {
        float: right;
        width: calc(75% - 11px);
        height: 400px;
        padding-left: 10px;
        border-left: 1px solid #000000;
        text-align: left;
      }
    }
  }
}
</style>

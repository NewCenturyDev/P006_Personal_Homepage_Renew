<template>
  <div class="mainProfile" id="profile">
    <div class="myPhotoContainer">
      <img class="myPhoto" width="350px" height="350px" :src="$store.state.profile.photo" />
      <div class="name">윤성민</div>
      <el-button class="github" type="primary" v-on:click="openGithub">
        {{ $store.state.profile.codename }}
      </el-button>
      <div class="presentation" v-html="$store.state.profile.presentation"></div>
    </div>
    <div class="myHistoryContainer">
      <div class="myHistoryTitle">My History</div>
      <div class="myHistory">
        <el-timeline>
          <el-timeline-item
            v-for="(activity, activityIndex) in $store.state.activities"
            :key="activityIndex"
            :timestamp="activity.timestamp">
            {{ activity.content }}
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

<template>
  <div class="mainProjects" id="projects">
    <div class="title">My Projects</div>
    <div class="myProjectContainer">
      <el-tabs v-model="activeTab">
        <el-tab-pane
          v-for="(projectList, projectListIndex) in projectLists"
          :key="projectListIndex"
          :name="projectList.typeName"
          :label="projectList.typeName">
            <div class="cardContainer"
              v-for="(project, projectIndex) in projectList.projects"
              :key="projectIndex">
              <el-card v-if="projectList.projects.length !== 0" shadow="hover" body-style="{ width: calc(100% - 50px); padding: 0; }">
                <div class="projectList">
                  <div class="projectImageContainer">
                    <img class="projectImage" :src="`../assets/projects/${project.image}`" />
                    <div class="projectBtnContainer">
                      <el-button class="projectBtn" type="plane" v-on:click="openGithub(project.link)">
                        Github 열기
                      </el-button>
                      <el-button class="projectBtn" type="plane" v-on:click="gotoDetail(projectIndex)">
                        자세히 보기
                      </el-button>
                    </div>
                  </div>
                  <div class="projectInfo">
                    <div class="projectTitle">{{ project.name }}</div>
                    <div class="projectDiscription" v-html="project.discription"></div>
                    <div class="projectStackContainer">
                      <div class="projectStack"
                        v-for="(stack, stackIndex) in project.stack"
                        :key="stackIndex">
                        {{ stack }}
                      </div>
                    </div>
                  </div>
                </div>
              </el-card>
              <div v-else>
                해당 분류에 속하는 프로젝트가 없습니다.
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainProjects',
  data() {
    return {
      activeTab: 'Web',
      projectLists: [
        {
          typeName: 'Web',
          projects: [
            {
              name: 'SCP Schools',
              image: null,
              discription: 'TCP School을 모방하여 만든 웹 페이지로써, 세종대학교 컴퓨터공학과 1학년 과정에서 배우는 내용들을 정리한 웹 페이지입니다.<br/>이 프로젝트를 진행하면서 HTML, CSS, Javascript에 익숙해졌습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'JQuery'],
            },
            {
              name: 'My Journal Express',
              image: null,
              discription: '동아리에서 3인 프로젝트 (기획/디자인/개발 중 제가 개발을 담당하였습니다.) 로 진행한 자신만의 저널을 만들 수 있는 웹 서비스로써, 이미지나 동영상, 텍스트를 화면상에 자유롭게 배치가 가능한 것이 특징입니다.<br/>이 프로젝트를 진행하며 REST API 및 Ajax 기술에 대해 상당 부분 이해할 수 있었습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'JQuery', 'Node.js', 'EJS', 'Express.js', 'MySQL', 'Docker'],
            },
            {
              name: 'DK-Zone',
              image: null,
              discription: '페이스북 형태의 SNS 웹 서비스로써, 처음으로 SPA 프레임워크와 UI 프레임워크를 사용하여 만들어 본 프로젝트입니다.<br/>이 프로젝트를 진행하면서, SPA Framework, Client-Side Rendering, Templete, View Component, SPA-router, 반응형 레이아웃 기술 및 기법에 대해 상당 부분 이해할 수 있었습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'Vue.js', 'Node.js', 'Express.js', 'MySQL', 'Docker'],
            },
            {
              name: `HyperTech99's Portpolio`,
              image: null,
              discription: '제 예전 포트폴리오 웹 페이지입니다.<br/>이 프로젝트를 진행하면서, Vue.js보다 좀 더 대중적인 React.js를 사용할 줄 알게 되었습니다. 포트폴리오이기에, 정적인 내용만을 보여준다고 생각하여 백엔드는 구현하지 않고 하드코딩을 통해 구현했었습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'React.js'],
            },
            {
              name: `Sejong HackerTon`,
              image: null,
              discription: '세종대학교 해커톤에서 4인 프로젝트로 진행한 AI 시각화 웹 페이지입니다.<br/>이 프로젝트를 진행하면서, Vue.js, Node.js, Express, MySQL에 완벽하게 숙달될 수 있었습니다. 덤으로, 서버 간 통신[임베디드 장치(Arduino) <-> AI Server(Python) <-> Web Backend(Node.js Express) <-> Web Frontend(Vue.js)]을 구현해 볼 수 있는 좋은 기회였습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'Vue.js', 'Node.js', 'Express', 'MySQL'],
            },
            {
              name: `HyperTech99's Page (The New Portpolio)`,
              image: null,
              discription: '제 현재 포트폴리오 웹 페이지입니다.<br/>하드코딩 특성상 내용 변경 및 유지보수에 불편함을 겪어 이 프로젝트를 진행하게 되었습니다. 이 프로젝트를 진행하면서, Spring Framework를 사용하여 API 백엔드를 구현하여 조금 더 편하게 포트폴리오를 관리할 수 있게 되었습니다.',
              stack: ['HTML5', 'CSS3', 'Javascript', 'Vue.js', 'JAVA Spring', 'Mybatis', 'MySQL', 'Docker'],
            },
            {
              name: `HyperTech99's Archive`,
              image: null,
              discription: 'DevoThink라는 프로그램의 기능에 영감을 받아 만든 온라인 아카이빙 웹 서비스입니다.<br/>이 프로젝트를 진행하면서, Spring Framework에 익숙해지고, JSP, Mybatis를 사용하는 방법을 깨닫게 되었습니다. Node.js를 이용한 단순한 API 서버 대신, Server-Side에서 MVC 모두를 다루어 보는 경험을 할 수 있었습니다. 조금 고전적인 기술이기는 하지만, Server Side Rendering과 Client Side Rendering의 장단점을 파악할 수 있는 기회가 되었습니다.',
              stack: ['HTML5', 'CSS3', 'JSP', 'Server-Side Rendering', 'JAVA Spring', 'Mybatis', 'MySQL', 'Docker', 'Jenkins'],
            },
            // {
            //   name: `HyperTech99's Storage`,
            //   image: null,
            //   discription: '서버의 파일들을 관리할 수 있는 웹 파일 탐색기 프로젝트입니다.<br/>이 프로젝트를 진행하면서, Spring Framework 및 Vue.js Framework에 매우 숙달될 수 있었습니다.',
            //   stack: ['HTML5', 'CSS3', 'Javascript', 'Vue.js', 'JAVA Spring', 'Spring Boot', 'Mybatis', 'MySQL', 'Docker', 'Jenkins'],
            // },
          ],
        },
        {
          typeName: 'Android',
          projects: [
            {
              name: 'JH-High App',
              image: null,
              discription: '',
              stack: ['Android', 'Native Android App'],
            },
            {
              name: 'My Journal Express Mobile',
              image: null,
              discription: '',
              stack: ['Android', 'Web App Sync'],
            },
            {
              name: 'DK-Zone Mobile',
              image: null,
              discription: '',
              stack: ['Android', 'Web App Sync'],
            },
            {
              name: 'Vega Conflict Central',
              image: null,
              discription: '',
              stack: ['Android', 'Native Android App'],
            },
          ],
        },
        {
          typeName: 'Etc.',
          projects: [
            {
              name: 'Jjapke-Mon',
              image: null,
              discription: '',
              stack: ['C++', 'Console Application', 'Game'],
            },
            {
              name: 'Jjaplu-Marble',
              image: null,
              discription: '',
              stack: ['JAVA', 'GUI Application', 'Swing', 'AWT', 'Game'],
            },
            {
              name: 'OSS-MineSweeper',
              image: null,
              discription: '',
              stack: ['C', 'Console Application', 'Git', 'TeamWork', 'Cleancode', 'Refactoring'],
            },
            
          ],
        },
      ]
    };
  },
  methods: {
    openGithub(link) {
      window.open(link);
    },
    gotoDetail(index) {
      this.$router.push({
        name: 'project',
        params: { index },
      });
    },
  }
}
</script>

<style lang="scss">
/* UI library override */
.mainProjects {
  .el-tabs__header {
    width: calc(100% - 50px) !important;
    margin: 0 25px !important;
  }
  .el-tabs__content {
    width: calc(100% - 50px) !important;
    margin: 0 25px !important;
  }
  .el-tabs__header is-top {
    margin: 0 !important;
  }
  .el-card {
    border-radius: 0px !important;
  }
  .el-button {
    border-left: 0 !important;
    border-right: 0 !important;
    border-top: 0 !important;
    border-bottom: 1px solid #ebeef5;
    border-radius: 0px !important;
  }
  .el-button+.el-button {
    margin: 0 !important;
  }
}
</style>

<style lang="scss" scoped>
.mainProjects {
  max-width: 1500px;
  padding: 50px calc(50% - 600px);
  background-color: #f0f8ff;
  .title {
    width: 100%;
    height: 50px;
    margin-bottom: 50px;
    font-size: 40px;
    line-height: 50px;
    text-align: center;
  }
  .myProjectContainer {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1200px;
    .cardContainer {
      margin: 15px 0;
      .projectList {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        width: 100%;
        .projectImageContainer {
          display: flex;
          flex-direction: column;
          flex-wrap: wrap;
          width: 310px;
          .projectImage {
            width: 310px;
            height: 200px;
          }
          .projectBtnContainer {
            width: 310px;
            display: flex;
            flex-direction: column;
            flex-wrap: wrap;
            justify-content: right;
            max-height: 180px;
            .projectBtn {
              width: 100%;
            }
          }
        }
        .projectInfo {
          min-width: 260px;
          max-width: 600px;
          margin: 10px 25px;
          .projectTitle {
            width: 100%;
            margin: 5px 0;
            text-align: left;
            font-size: 28px;
            line-height: 35px;
          }
          .projectDiscription {
            width: 100%;
            margin: 15px 0;
            text-align: left;
            font-size: 15px;
            line-height: 20px;
          }
          .projectStackContainer {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            width: 100%;
            text-align: left;
            font-size: 12px;
            color: #bbbbbb;
            line-height: 15px;
            .projectStack {
              margin-right: 10px;
            }
          }
        }
      }
    }
  }
}
</style>

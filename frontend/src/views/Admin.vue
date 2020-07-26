<template>
  <div class="admin">
    <el-page-header class="header" @back="goHome" title="Home" content="포트폴리오 관리"></el-page-header>
    <el-divider class="headerDivider"></el-divider>
    <el-card class="settingContainer">
      <el-header class="settingTitle">
        Profile
        <el-button class="logoutBtn" v-on:click="logout">로그아웃</el-button>
      </el-header>
      <div class="settingOption">개인사진 설정</div>
      <input type="file" ref="profilePhoto" v-on:change="selectProfilePhoto()"/>
      <el-button class="confirmBtn" v-on:click="setProfilePhoto()" size="small" type="primary">업로드</el-button>
      <div class="settingOption">코드네임 설정</div>
      <el-input
        placeholder="코드네임"
        v-model="newCodename">
      </el-input>
      <el-button class="confirmBtn" v-on:click="setCodename" size="small" type="primary">설정</el-button>
      <div class="settingOption">자기소개 문구 설정 (HTML 지원)</div>
      <el-input
        type="textarea"
        :rows="3"
        placeholder="자기소개"
        v-model="newPresentation">
      </el-input>
      <el-button class="confirmBtn" v-on:click="setPresentation" size="small" type="primary">설정</el-button>
      <div class="settingOption">활동 이력 관리</div>
      <el-table
        ref="activityTable"
        :data="$store.state.activities">
        <el-table-column
          property="id"
          label="ID"
          width="60">
        </el-table-column>
        <el-table-column
          property="content"
          label="Content">
        </el-table-column>
        <el-table-column
          property="timestamp"
          label="Timestamp"
          width="120">
        </el-table-column>
        <el-table-column width="160" label="Operation">
          <template slot-scope="activityScope">
            <el-button class="editBtn" size="mini" type="primary" v-on:click="selectActivity(activityScope.$index)">수정</el-button>
            <el-popconfirm class="deleteBtn"
              title="정말 활동이력을 삭제하시겠습니까?"
              confirmButtonText='삭제'
              cancelButtonText='취소'
              v-on:onConfirm="deleteActivity($store.state.activities[activityScope.$index].id)">
              <el-button size="mini" type="danger" slot="reference">삭제</el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-button class="confirmBtn" size="small" type="success" v-on:click="activityFormOpen = true">추가</el-button>
      <el-dialog class="activityForm"
        :close-on-click-modal="false"
        v-on:close="clearNewActivityInput"
        :visible.sync="activityFormOpen">
        <el-input class="activityContent" placeholder="활동 내용" v-model="newActivity.content"></el-input>
        <el-input class="activityTimestamp" placeholder="활동 일자 (YYYY. MM. DD 형식 권장)" v-model="newActivity.timestamp"></el-input>
        <el-button v-on:click="createActivity" v-if="newActivity.id === null" type="primary">설정</el-button>
        <el-button v-on:click="modifyActivity" v-else type="primary">수정</el-button>
        <el-button v-on:click="clearNewActivityInput">취소</el-button>
      </el-dialog>
    </el-card>
    <el-card class="settingContainer">
      <el-header class="settingTitle">Skills</el-header>
      <div class="settingOption">기술스택 카테고리 관리</div>
      <div class="categoryContainer">
        <el-card class="category"
          v-for="(skillCategory, skillCategoryIndex) in $store.state.skillCategory"
          :key="skillCategoryIndex">
          <div class="categoryName">{{ skillCategory.category }}</div>
          <el-button v-on:click="selectSkillCategory(skillCategory)" size="mini" type="plane">수정</el-button>
          <el-popconfirm
            title="정말 카테고리를 삭제하시겠습니까?"
            confirmButtonText='삭제'
            cancelButtonText='취소'
            v-on:onConfirm="deleteSkillCategory(skillCategory.id)">
            <el-button size="mini" type="plane" slot="reference">삭제</el-button>
          </el-popconfirm>
        </el-card>
      </div>
      <el-button class="confirmBtn" size="small" type="success" v-on:click="skillCategoryFormOpen = true">카테고리 추가</el-button>
      <el-dialog class="categoryForm"
        :close-on-click-modal="false"
        v-on:close="clearNewSkillCategoryInput"
        :visible.sync="skillCategoryFormOpen">
        <el-input class="categoryName" placeholder="새 카테고리 이름" v-model="newSkillCategory.category"></el-input>
        <el-button v-on:click="createSkillCategory" v-if="newSkillCategory.id === null" type="primary">추가</el-button>
        <el-button v-on:click="modifySkillCategory" v-else type="primary">수정</el-button>
        <el-button v-on:click="clearNewSkillCategoryInput">취소</el-button>
      </el-dialog>
      <div class="settingOption">기술스택 목록 관리</div>
      <el-table
        ref="skillTable"
        :data="$store.state.skills">
        <el-table-column
          property="id"
          label="ID"
          width="60">
        </el-table-column>
        <el-table-column
          property="category"
          label="Category"
          width="120">
        </el-table-column>
        <el-table-column
          property="name"
          label="Name">
        </el-table-column>
        <el-table-column width="160" label="Operation">
          <template slot-scope="skillScope">
            <el-button class="editBtn" size="mini" type="primary" v-on:click="selectSkill(skillScope.$index)">수정</el-button>
            <el-popconfirm class="deleteBtn"
              title="정말 기술스택을 삭제하시겠습니까?"
              confirmButtonText='삭제'
              cancelButtonText='취소'
              v-on:onConfirm="deleteSkill($store.state.skills[skillScope.$index].id)">
              <el-button size="mini" type="danger" slot="reference">삭제</el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-button class="confirmBtn" size="small" type="success" v-on:click="skillFormOpen = true">추가</el-button>
      <el-dialog class="skillForm"
        :close-on-click-modal="false"
        v-on:close="clearNewSkillInput"
        :visible.sync="skillFormOpen">
        <el-select class="skillCategory" v-model="newSkill.category" placeholder="카테고리">
          <el-option
            v-for="(skillCategory, skillCategoryIndex) in $store.state.skillCategory"
            :key="skillCategoryIndex"
            :label="skillCategory.category"
            :value="skillCategory.category">
          </el-option>
        </el-select>
        <input class="skillImage" type="file" placeholder="기술스택 이미지" ref="skillImage" v-on:change="selectSkillImage()"/>
        <el-input class="skillName" placeholder="기술스택명" v-model="newSkill.name"></el-input>
        <el-button type="primary" v-on:click="createSkill" v-if="newSkill.id === null">추가</el-button>
        <el-button type="primary" v-on:click="modifySkill" v-else>수정</el-button>
        <el-button v-on:click="clearNewSkillInput">취소</el-button>
      </el-dialog>
    </el-card>
    <el-card class="settingContainer">
      <el-header class="settingTitle">Projects</el-header>
      <div class="settingOption">프로젝트 카테고리</div>
      <div class="categoryContainer">
        <el-card class="category"
          v-for="(projectCategory, projectCategoryIndex) in $store.state.projectCategory"
          :key="projectCategoryIndex">
          <div class="categoryName">{{ projectCategory }}</div>
          <el-button v-on:click="selectProjectCategory(projectCategory)" size="mini" type="plane">수정</el-button>
          <el-popconfirm
            title="정말 카테고리를 삭제하시겠습니까?"
            confirmButtonText='삭제'
            cancelButtonText='취소'
            v-on:onConfirm="deleteProjectCategory(projectCategory)">
            <el-button size="mini" type="plane" slot="reference">삭제</el-button>
          </el-popconfirm>
        </el-card>
      </div>
      <el-button class="confirmBtn" size="small" type="success" v-on:click="projectCategoryFormOpen = true">카테고리 추가</el-button>
      <el-dialog class="categoryForm"
        :close-on-click-modal="false"
        v-on:close="clearNewProjectCategoryInput"
        :visible.sync="projectCategoryFormOpen">
        <el-input class="categoryName" placeholder="새 카테고리 이름" v-model="newProjectCategory"></el-input>
        <el-button class="confirmBtn" v-on:click="setProjectCategory" type="primary">추가</el-button>
        <el-button v-on:click="clearNewProjectCategoryInput">취소</el-button>
      </el-dialog>
      <div class="settingOption">프로젝트 목록</div>
      <el-table
        ref="projectTable"
        :data="$store.state.projects">
        <el-table-column
          property="id"
          label="ID"
          width="60">
        </el-table-column>
        <el-table-column
          property="category"
          label="Category"
          width="120">
        </el-table-column>
        <el-table-column
          property="name"
          label="Name"
          width="200">
        </el-table-column>
        <el-table-column
          property="link"
          label="Link"
          width="200">
        </el-table-column>
        <el-table-column
          label="Discription"
          width="500">
          <template slot-scope="projectScope">
            <div v-html="$store.state.projects[projectScope.$index].discription"></div>
          </template>
        </el-table-column>
        <el-table-column
          label="Stack Tags"
          width="200">
          <template slot-scope="projectScope">
            <el-tag class="tag"
              v-for="(tag, tagIndex) in $store.state.projects[projectScope.$index].stackTags"
              :key="tagIndex"
              size="mini">
              {{ tag }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column width="160" label="Operation">
          <template slot-scope="projectScope">
            <el-button class="showBtn" size="mini">내용 보기</el-button>
            <el-button class="editBtn" size="mini" type="primary" v-on:click="selectProject(projectScope.$index)">수정</el-button>
            <el-popconfirm
              title="정말 프로젝트를 삭제하시겠습니까?"
              confirmButtonText='삭제'
              cancelButtonText='취소'
              v-on:onConfirm="deleteProject($store.state.projects[projectScope.$index].id)">
              <el-button size="mini" type="danger" slot="reference">삭제</el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-button class="confirmBtn" size="small" type="success" v-on:click="projectFormOpen = true">추가</el-button>
      <el-dialog class="projectForm"
        :close-on-click-modal="false"
        v-on:close="clearNewProjectInput"
        :visible.sync="projectFormOpen">
        <el-select class="projectCategory" v-model="newProject.category" placeholder="카테고리">
          <el-option
            v-for="(projectCategory, projectCategoryIndex) in $store.state.projectCategory"
            :key="projectCategoryIndex"
            :label="projectCategory"
            :value="projectCategory">
          </el-option>
        </el-select>
        <el-input class="projectName" placeholder="프로젝트명" v-model="newProject.name"></el-input>
        <el-input class="projectLink" placeholder="프로젝트 Repo URL" v-model="newProject.link"></el-input>
        <el-input class="projectStack" placeholder="프로젝트 기술스택 (쉼표로 구분)" v-model="newProject.stackTags"></el-input>
        <el-input class="projectSummery"
          placeholder="프로젝트 개요"
          type="textarea"
          :rows="5"
          v-model="newProject.discription"></el-input>
        <v-md-editor class="projectContent" mode="editable" v-model="newProject.content" height="500px"></v-md-editor>
        <input class="projectImage" type="file" multiple placeholder="기술스택 이미지" ref="projectScreenshot" v-on:change="selectProjectImage()"/>
        <el-button type="primary" v-on:click="createProject" v-if="newProject.id === null">추가</el-button>
        <el-button type="primary" v-on:click="modifyProject" v-else>수정</el-button>
        <el-button v-on:click="clearNewProjectInput">취소</el-button>
      </el-dialog>
    </el-card>
    <div class="footer">Made by. 윤성민</div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Admin',
  data() {
    return {
      newCodename: this.$store.state.profile.codename,
      newPresentation: this.$store.state.profile.presentation,
      newProfilePhoto: null,
      activityFormOpen: false,
      newActivity: {
        id: null,
        content: '',
        timestamp: '',
      },
      skillFormOpen: false,
      skillCategoryFormOpen: false,
      newSkillCategory: {
        id: null,
        category: '',
      },
      newSkill: {
        id: null,
        name: '',
        category: '',
        image: null,
      },
      projectFormOpen: false,
      projectCategoryFormOpen: false,
      newProjectCategory: '',
      newProject: {
        id: null,
        category: '',
        name: '',
        link: '',
        screenshot: [],
        discription: '',
        stackTags: '',
        content: '',
      },
    };
  },
  async beforeMount() {
    try {
      const isLoggedIn = await this.$store.dispatch('checkSession');
      if (isLoggedIn === false) {
        this.$router.push('/');
      }
    } catch (error) {
      alert(error);
    }
  },
  methods: {
    goHome() {
      this.$router.push('/');
    },
    async logout() {
      await this.$store.dispatch('logout');
      this.goHome();
    },
    async setCodename() {
      try {
        await this.$store.dispatch('setCodename', this.newCodename);
      } catch (error) {
        alert(error);
      }
    },
    async setPresentation() {
      try {
        await this.$store.dispatch('setPresentation', this.newPresentation);
      } catch (error) {
        alert(error);
      }
    },
    selectProfilePhoto() {
      this.newProfilePhoto = this.$refs.profilePhoto.files[0];
    },
    async setProfilePhoto() {
      try {
        await this.$store.dispatch('setProfilePhoto', this.newProfilePhoto);
      } catch (error) {
        alert(error);
      }
    },
    selectActivity(activityIndex) {
      this.newActivity = this.$store.state.activities[activityIndex];
      this.activityFormOpen = true;
    },
    async createActivity() {
      try {
        await this.$store.dispatch('createActivity', this.newActivity);
        this.clearNewActivityInput();
      } catch (error) {
        alert(error);
      }
    },
    async modifyActivity() {
      try {
        await this.$store.dispatch('modifyActivity', this.newActivity);
        this.clearNewActivityInput();
      } catch (error) {
        alert(error);
      }
    },
    async deleteActivity(activityID) {
      try {
        await this.$store.dispatch('deleteActivity', activityID);
      } catch (error) {
        alert(error);
      }
    },
    clearNewActivityInput() {
      this.newActivity = '';
      this.activityFormOpen = false;
    },
    selectSkillCategory(category) {
      this.newSkillCategory = category;
      this.skillCategoryFormOpen = true;
    },
    async createSkillCategory() {
      try {
        await this.$store.dispatch('createSkillCategory', this.newSkillCategory);
        this.clearNewSkillCategoryInput();
      } catch (error) {
        alert(error);
      }
    },
    async modifySkillCategory() {
      try {
        await this.$store.dispatch('modifySkillCategory', this.newSkillCategory);
        this.clearNewSkillCategoryInput();
      } catch (error) {
        alert(error);
      }
    },
    async deleteSkillCategory(categoryID) {
      try {
        await this.$store.dispatch('deleteSkillCategory', categoryID);
      } catch (error) {
        alert(error);
      }
    },
    clearNewSkillCategoryInput() {
      this.newSkillCategory = {
        id: null,
        category: '',
      };
      this.skillCategoryFormOpen = false;
    },
    selectSkill(skillIndex) {
      this.newSkill = this.$store.state.skills[skillIndex];
      this.skillFormOpen = true;
    },
    async createSkill() {
      try {
        await this.$store.dispatch('createSkill', this.newSkill);
        this.clearNewSkillInput();
      } catch (error) {
        alert(error);
      }
    },
    async modifySkill() {
      try {
        await this.$store.dispatch('modifySkill', this.newSkill);
        this.clearNewSkillInput();
      } catch (error) {
        alert(error);
      }
    },
    async deleteSkill(skillID) {
      try {
        await this.$store.dispatch('deleteSkill', skillID);
      } catch (error) {
        alert(error);
      }
    },
    selectSkillImage() {
      this.newSkill.image = this.$refs.skillImage.files[0];
    },
    clearNewSkillInput() {
      this.newSkill = {
        id: null,
        name: '',
        category: '',
        image: null,
      };
      this.$refs.skillImage.value = null;
      this.skillFormOpen = false;
    },
    selectProjectCategory(category) {
      this.newProjectCategory = category;
      this.projectCategoryFormOpen = true;
    },
    async setProjectCategory(){
      try {
        await this.$store.dispatch('setProjectCategory', this.newProjectCategory);
      } catch (error) {
        alert(error);
      }
    },
    async deleteProjectCategory(category) {
      try {
        await this.$store.dispatch('deleteProjectCategory', category);
      } catch (error) {
        alert(error);
      }
    },
    clearNewProjectCategoryInput() {
      this.newProjectCategory = '';
      this.projectCategoryFormOpen = false;
    },
    selectProject(projectIndex) {
      this.newProject = this.$store.state.projects[projectIndex];
      this.projectFormOpen = true;
    },
    async createProject() {
      try {
        await this.$store.dispatch('createProject', this.newProject);
      } catch (error) {
        alert(error);
      }
    },
    async modifyProject() {
      try {
        await this.$store.dispatch('modifyProject', this.newProject);
      } catch (error) {
        alert(error);
      }
    },
    async deleteProject(projectID) {
      try {
        await this.$store.dispatch('deleteProject', projectID);
      } catch (error) {
        alert(error);
      }
    },
    selectProjectImage() {
      this.newProject.screenshot = this.$refs.projectScreenshot.files[0];
    },
    clearNewProjectInput() {
      this.newProject = {
        id: null,
        category: '',
        name: '',
        link: '',
        screenshot: [],
        discription: '',
        stackTags: '',
        content: '',
      };
      this.$refs.projectScreenshot.value = null;
      this.projectFormOpen = false;
    },
  }
}
</script>

<style lang="scss">
/* UI Library CSS Override */
.admin {
  .el-dialog {
    width: 100% !important;
    margin: 0 !important;
    .el-dialog__header {
      padding: 0 !important;
    }
  }
  .category {
    .el-card__body {
      padding: 5px !important;
    }
    .el-button {
      border: 0 !important;
      font-size: 10px;
    }
  }
}
</style>

<style lang="scss" scoped>
.admin {
  padding: 0 25px;
  background-color: #eeeeee;
  .header {
    height: 50px;
    padding: 0 25px;
    margin: 0 -25px;
    font-size: 25px;
    line-height: 50px;
    background-color: #ffffff;
  }
  .headerDivider {
    width: calc(100% + 50px);
    margin: 0 -25px !important;
  }
  .settingContainer {
    max-width: 1000px;
    margin: 25px auto;
    .settingTitle {
      font-size: 25px;
      line-height: 50px;
      font-weight: bold;
    }
    .settingOption {
      margin-top: 30px;
      margin-bottom: 10px;
      font-size: 16px;
      font-weight: bold;
      text-align: left;
    }
    .logoutBtn {
      float: right;
      margin: 10px;
    }
    .confirmBtn {
      margin: 10px;
    }
    .editBtn, .deleteBtn {
      margin: 5px;
    }
    .showBtn {
      width: 117.5px;
      margin: 5px;
    }
    .tag {
      margin: 5px;
      font-size: 8px;
    }
    .categoryContainer {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: center;
      .category {
        margin: 5px;
        .categoryName {
          font-size: 15px;
          font-weight: bold;
          line-height: 20px;
        }
      }
    }
  }
  .activityForm {
    max-width: 600px;
    margin: 150px auto;
    .activityContent {
      width: calc(100% - 30px);
      margin: 15px;
    }
    .activityTimestamp {
      width: calc(100% - 30px);
      margin: 15px;
    }
  }
  .categoryForm {
    max-width: 500px;
    margin: 150px auto;
    .categoryName {
      width: calc(100% - 30px);
      margin: 25px 15px;
    }
  }
  .skillForm {
    max-width: 600px;
    margin: 150px auto;
    .skillCategory {
      width: calc(50% - 20px);
      margin-left: 15px;
      margin-right: 5px;
    }
    .skillImage {
      width: calc(50% - 20px);
      min-height: 40px;
      margin-left: 5px;
      margin-right: 15px;
    }
    .skillName {
      width: calc(100% - 30px);
      margin: 15px;
    }
  }
  .projectForm {
    max-width: 1000px;
    margin: 25px auto;
    .projectCategory {
      float: left;
      width: 120px;
      margin: 5px 0;
      margin-left: 15px;
      margin-right: 5px;
    }
    .projectName {
      width: calc(100% - 160px);
      margin: 5px 0;
      margin-left: 5px;
      margin-right: 15px;
    }
    .projectLink {
      width: calc(50% - 20px);
      margin: 5px 0;
      margin-left: 15px;
      margin-right: 5px;
    }
    .projectStack {
      width: calc(50% - 20px);
      margin: 5px 0;
      margin-left: 5px;
      margin-right: 15px;
    }
    .projectSummery {
      width: calc(100% - 30px);
      margin: 5px 15px;
    }
    .projectContent {
      width: calc(100% - 30px);
      margin: 5px 15px;
      text-align: left;
    }
    .projectImage {
      width: calc(100% - 30px);
      min-height: 40px;
      margin: 5px 15px;
    }
  }
  .footer {
    height: 50px;
    font-size: 12px;
    font-weight: bold;
    line-height: 20px;
  }
}
</style>

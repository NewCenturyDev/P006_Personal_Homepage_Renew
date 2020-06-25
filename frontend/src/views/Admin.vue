<template>
  <div class="admin">
    <el-card>
      <el-header>Profile</el-header>
      <div>개인사진</div>
      <input type="file" ref="profilePhoto" v-on:change="setProfilePhoto()"/>
      <el-button v-on:click="uploadProfilePhoto()" size="mini" type="primary">업로드</el-button>
      <div>코드네임</div>
      <el-input
        placeholder="코드네임"
        v-model="codename">
      </el-input>
      <div>자기소개</div>
      <el-input
        type="textarea"
        :rows="3"
        placeholder="자기소개"
        v-model="presentation">
      </el-input>
    </el-card>
    <el-card>
      <el-header>Skills</el-header>
      <div>기술스택 카테고리</div>
      <div class="skillCategoryContainer">
        <el-card
          v-for="(skillCategory, skillCategoryIndex) in $store.state.skillCategory"
          :key="skillCategoryIndex">
          <div>{{ skillCategory }}</div>
          <el-button v-on:click="modifySkillCategory(skillCategory)" size="mini" type="primary">수정</el-button>
          <el-popconfirm
            title="정말 카테고리를 삭제하시겠습니까?"
            confirmButtonText='삭제'
            cancelButtonText='취소'
            v-on:onConfirm="deleteSkillCategory(skillCategory)">
            <el-button size="mini" type="danger" slot="reference">삭제</el-button>
          </el-popconfirm>
        </el-card>
      </div>
      <el-button type="success" v-on:click="skillCategoryFormOpen = true">카테고리 추가</el-button>
      <el-dialog class="skillCategoryForm"
        v-on:close="clearNewSkillCategoryInput"
        :visible.sync="skillCategoryFormOpen">
        <el-input placeholder="새 카테고리 이름" v-model="newSkillCategory"></el-input>
        <el-button v-on:click="createSkillCategory" type="primary">추가</el-button>
        <el-button v-on:click="clearNewSkillCategoryInput">취소</el-button>
      </el-dialog>
      <div>기술스택 목록</div>
      <el-table
        ref="skillTable"
        :data="$store.state.skills">
        <el-table-column
          type=index
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
        <el-table-column width="150" label="Operation">
          <template slot-scope="skillScope">
            <el-button size="mini" type="primary" v-on:click="selectSkill(skillScope.$index)">수정</el-button>
            <el-popconfirm
              title="정말 기술스택을 삭제하시겠습니까?"
              confirmButtonText='삭제'
              cancelButtonText='취소'
              v-on:onConfirm="deleteSkill(skillScope.$index)">
              <el-button size="mini" type="danger" slot="reference">삭제</el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="success" v-on:click="skillFormOpen = true">추가</el-button>
      <el-dialog class="skillForm"
        v-on:close="clearNewSkillInput"
        :visible.sync="skillFormOpen">
        <el-select v-model="newSkill.category" placeholder="카테고리">
          <el-option
            v-for="(skillCategory, skillCategoryIndex) in $store.state.skillCategory"
            :key="skillCategoryIndex"
            :label="skillCategory"
            :value="skillCategory">
          </el-option>
        </el-select>
        <el-input placeholder="기술스택명" v-model="newSkill.name"></el-input>
        <input type="file" placeholder="기술스택 이미지" ref="skillImage" v-on:change="setSkillImage()"/>
        <el-button type="primary" v-on:click="createSkill" v-if="newSkill.id === null">추가</el-button>
        <el-button type="primary" v-on:click="modifySkill" v-else>수정</el-button>
        <el-button v-on:click="clearNewSkillInput">취소</el-button>
      </el-dialog>
    </el-card>
    <el-card>
      <el-header>Projects</el-header>
      <div>프로젝트 카테고리</div>
      <div class="projectCategoryContainer">
        <el-card
          v-for="(projectCategory, projectCategoryIndex) in $store.state.projectCategory"
          :key="projectCategoryIndex">
          <div>{{ projectCategory }}</div>
          <el-button v-on:click="modifyProjectCategory(projectCategory)" size="mini" type="primary">수정</el-button>
          <el-popconfirm
            title="정말 카테고리를 삭제하시겠습니까?"
            confirmButtonText='삭제'
            cancelButtonText='취소'
            v-on:onConfirm="deleteProjectCategory(projectCategory)">
            <el-button size="mini" type="danger" slot="reference">삭제</el-button>
          </el-popconfirm>
        </el-card>
      </div>
      <el-button type="success" v-on:click="projectCategoryFormOpen = true">카테고리 추가</el-button>
      <el-dialog class="projectCategoryForm"
        v-on:close="clearNewProjectCategoryInput"
        :visible.sync="projectCategoryFormOpen">
        <el-input placeholder="새 카테고리 이름" v-model="newProjectCategory"></el-input>
        <el-button v-on:click="createProjectCategory" type="primary">추가</el-button>
        <el-button v-on:click="clearNewProjectCategoryInput">취소</el-button>
      </el-dialog>
      <div>프로젝트 목록</div>
      <el-table
        ref="projectTable"
        :data="$store.state.projects">
        <el-table-column
          type=index
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
          property="discription"
          label="Discription"
          width="200">
        </el-table-column>
        <el-table-column
          property="stackTags"
          label="Stack Tags"
          width="200">
        </el-table-column>
        <el-table-column width="150" label="Operation">
          <template slot-scope="projectScope">
            <el-button size="mini">내용 보기</el-button>
            <el-button size="mini" type="primary" v-on:click="selectProject(projectScope.$index)">수정</el-button>
            <el-popconfirm
              title="정말 기술스택을 삭제하시겠습니까?"
              confirmButtonText='삭제'
              cancelButtonText='취소'
              v-on:onConfirm="deleteProject(projectScope.$index)">
              <el-button size="mini" type="danger" slot="reference">삭제</el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="success" v-on:click="projectFormOpen = true">추가</el-button>
      <el-dialog class="projectForm"
        v-on:close="clearNewProjectInput"
        :visible.sync="projectFormOpen">
        <el-select v-model="newProject.category" placeholder="카테고리">
          <el-option
            v-for="(projectCategory, projectCategoryIndex) in $store.state.projectCategory"
            :key="projectCategoryIndex"
            :label="projectCategory"
            :value="projectCategory">
          </el-option>
        </el-select>
        <el-input placeholder="프로젝트명" v-model="newProject.name"></el-input>
        <el-input placeholder="프로젝트 Repo URL" v-model="newProject.link"></el-input>
        <el-input placeholder="프로젝트 개요" v-model="newProject.discription"></el-input>
        <el-input placeholder="프로젝트 기술스택 (쉼표로 구분)" v-model="newProject.stackTags"></el-input>
        <v-md-editor class="editor" mode="editable" v-model="newProject.content" height="400px"></v-md-editor>
        <el-button v-on:click="check">테스트</el-button>
        <input type="file" multiple placeholder="기술스택 이미지" ref="projectScreenshot" v-on:change="setProjectImage()"/>
        <el-button type="primary" v-on:click="createProject" v-if="newProject.id === null">추가</el-button>
        <el-button type="primary" v-on:click="modifyProject" v-else>수정</el-button>
        <el-button v-on:click="clearNewProjectInput">취소</el-button>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Admin',
  data() {
    return {
      codename: '',
      presentation: '',
      newProfilePhoto: null,
      skillFormOpen: false,
      skillCategoryFormOpen: false,
      newSkillCategory: '',
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
  methods: {
    check() {
      //eslint-disable-next-line
      console.log(this.text);
    },
    handleUploadImage(event, insertImage, files) {
      // Get the files and upload them to the file server, then insert the corresponding content into the editor
      console.log(files);

      // Here is just an example
      insertImage({
        url:
          '',
        desc: 'desc',
      });
    },
    setProfilePhoto() {
      this.newProfilePhoto = this.$refs.profilePhoto.files[0];
    },
    uploadProfilePhoto() {
    },
    selectSkill(index) {
      this.newSkill = this.$store.state.skills[index];
      this.skillFormOpen = true;
    },
    createSkill() {
    },
    modifySkill() {
    },
    deleteSkill(index) {
      alert(index);
    },
    createSkillCategory(){
    },
    modifySkillCategory(category) {
      this.newSkillCategory = category;
      this.skillCategoryFormOpen = true;
    },
    deleteSkillCategory(category) {
      alert(category);
    },
    setSkillImage() {
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
    clearNewSkillCategoryInput() {
      this.newSkillCategory = '';
      this.skillCategoryFormOpen = false;
    },
    selectProject(index) {
      this.newProject = this.$store.state.projects[index];
      this.projectFormOpen = true;
    },
    createProject() {
    },
    modifyProject() {
    },
    deleteProject(index) {
      alert(index);
    },
    createProjectCategory(){
    },
    modifyProjectCategory(category) {
      this.newProjectCategory = category;
      this.projectCategoryFormOpen = true;
    },
    deleteProjectCategory(category) {
      alert(category);
    },
    setProjectImage() {
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
    clearNewProjectCategoryInput() {
      this.newProjectCategory = '';
      this.projectCategoryFormOpen = false;
    }
  }
}
</script>

<style lang="scss" scoped>
.admin {
  .editor {
    text-align: left;
  }
}
</style>

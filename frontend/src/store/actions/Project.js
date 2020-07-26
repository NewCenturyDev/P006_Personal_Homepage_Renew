import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async getProjectCategory (context) {
    try {
      const response = await Vue.axios.get(`${backendURL}/getProjectCategory`);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('loadProjectCategory', response.data.projectCategoryList);
    } catch (error) {
      throw error;
    }
  },
  async createProjectCategory (context, projectCategory) {
    try {
      if (projectCategory.category.length === 0) {
        throw '프로젝트 카테고리명을 입력해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/createProjectCategory`, projectCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createProjectCategory', response.data.projectCategory);
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifyProjectCategory (context, projectCategory) {
    try {
      if (projectCategory.category.length === 0) {
        throw '프로젝트 카테고리명을 입력해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/modifyProjectCategory`, projectCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifyProjectCategory', response.data.projectCategory);
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteProjectCategory (context, projectCategoryID) {
    try {
      if (typeof projectCategoryID !== 'number' || projectCategoryID < 1) {
        throw '잘못된 카테고리 ID 입니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteProjectCategory`, {id: projectCategoryID});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteProjectCategory', projectCategoryID);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async createProject (context, project) {
    if (project.name.length === 0) {
      throw '프로젝트 이름을 입력해 주십시오';
    }
    if (project.category.length === 0) {
      throw '프로젝트 카테고리를 선택해 주십시오';
    }
    if (project.link.length === 0) {
      throw '프로젝트 Github 리포지토리 주소를 입력해 주십시오';
    }
    if (project.discription.length === 0) {
      throw '프로젝트 개요를 입력해 주십시오';
    }
    if (project.screenshot[0] === null) {
      throw '프로젝트 스크린샷을 1장 이상 첨부해 주십시오';
    }
    if (project.content.length === 0) {
      throw '프로젝트 상세설명을 입력해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/createProject`, project);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createProject', response.data.project);  // projectObject
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifyProject (context, project) {
    if (project.name.length === 0) {
      throw '프로젝트 이름을 입력해 주십시오';
    }
    if (project.category.length === 0) {
      throw '프로젝트 카테고리를 선택해 주십시오';
    }
    if (project.link.length === 0) {
      throw '프로젝트 Github 리포지토리 주소를 입력해 주십시오';
    }
    if (project.discription.length === 0) {
      throw '프로젝트 개요를 입력해 주십시오';
    }
    if (project.screenshot[0] === null) {
      throw '프로젝트 스크린샷을 1장 이상 첨부해 주십시오';
    }
    if (project.content.length === 0) {
      throw '프로젝트 상세설명을 입력해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/modifyProject`, project);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifyProject', response.data.project);  // projectObject
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteProject (context, projectID) {
    try {
      if (typeof projectID !== 'number' || projectID < 1) {
        throw 'project 오브젝트의 ID가 잘못되었습니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteProject`, projectID);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteProject', projectID);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
};

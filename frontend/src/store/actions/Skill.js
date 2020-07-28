import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async getSkillCategory (context) {
    try {
      const response = await Vue.axios.get(`${backendURL}/getSkillCategory`);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('loadSkillCategory', response.data.skillCategoryList);
    } catch (error) {
      throw error;
    }
  },
  async createSkillCategory (context, skillCategory) {
    try {
      if (skillCategory.category.length === 0) {
        throw '기술스택 카테고리명을 입력해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/createSkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createSkillCategory', response.data.skillCategory);
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifySkillCategory (context, skillCategory) {
    try {
      if (skillCategory.category.length === 0) {
        throw '기술스택 카테고리명을 입력해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/modifySkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifySkillCategory', response.data.skillCategory);
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteSkillCategory (context, skillCategoryID) {
    try {
      if (typeof skillCategoryID !== 'number' || skillCategoryID < 1) {
        throw '잘못된 카테고리 ID 입니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteSkillCategory`, {id: skillCategoryID});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteSkillCategory', skillCategoryID);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async getSkillList (context) {
    try {
      const response = await Vue.axios.get(`${backendURL}/getSkillList`);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('loadSkillList', response.data.skillList);
    } catch (error) {
      throw error;
    }
  },
  async createSkill (context, skill) {
    if (skill.name.length === 0) {
      throw '기술스택 이름을 입력해 주십시오';
    }
    if (skill.image === null) {
      throw '기술스택 이미지를 첨부해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/createSkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      const formData = new FormData();
      formData.append('file', skill.image);
      formData.append('skillID', response.data.skillID[0]);
      const fileUploadResponse = await Vue.axios.post(`${backendURL}/uploadSkillImage`, formData);
      if (fileUploadResponse.data.status.success === false) {
        throw fileUploadResponse.data.status.message;
      }
      context.commit('createSkill', fileUploadResponse.data.skill);  //skillObject
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifySkill (context, skill) {
    if (skill.name.length === 0) {
      throw '기술스택 이름을 입력해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/modifySkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      if (typeof skill.image === 'object') {
        const formData = new FormData();
        formData.append('file', skill.image);
        formData.append('skillID', response.data.skill.id);
        const fileUploadResponse = await Vue.axios.post(`${backendURL}/uploadSkillImage`, formData);
        if (fileUploadResponse.data.status.success === false) {
          throw fileUploadResponse.data.status.message;
        }
        context.commit('modifySkill', fileUploadResponse.data.skill);  //skillObject
      }
      else {
        context.commit('modifySkill', response.data.skill);  //skillObject
      }
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteSkill (context, skillID) {
    try {
      if (typeof skillID !== 'number' || skillID < 1) {
        throw 'skill 오브젝트의 ID가 잘못되었습니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteSkill`, {id: skillID});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteSkill', skillID);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
};

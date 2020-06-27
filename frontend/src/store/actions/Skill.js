import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async setSkillCategory (context, skillCategory) {
    try {
      if (skillCategory.length === 0) {
        throw '기술스택 카테고리를 입력해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/setSkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setSkillCategory', skillCategory);
      alert('설정되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteSkillCategory (context, skillCategory) {
    try {
      if (skillCategory === '') {
        throw '잘못된 카테고리입니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteSkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteSkillCategory', skillCategory);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async createSkill (context, skill) {
    if (skill.name.length === 0) {
      throw '기술스택 이름을 입력해 주십시오';
    }
    if (skill.image === null) {
      throw '기술스택 스크린샷을 1장 이상 첨부해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/createSkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createSkill', response.data.skill);  //skillObject
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifySkill (context, skill) {
    if (skill.name.length === 0) {
      throw '기술스택 이름을 입력해 주십시오';
    }
    if (skill.image === null) {
      throw '기술스택 스크린샷을 1장 이상 첨부해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/modifySkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifySkill', response.data.skill);  //skillObject
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
      const response = await Vue.axios.post(`${backendURL}/deleteSkill`, skillID);
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

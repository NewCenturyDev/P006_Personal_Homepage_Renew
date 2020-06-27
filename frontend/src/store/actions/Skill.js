import Vue from 'vue';
import '../../plugins/host';

export default {
  async setSkillCategory (context, skillCategory) {
    try {
      const response = await Vue.axios.post(`${backendURL}/setSkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setSkillCategory', skillCategory);
    } catch (error) {
      throw error;
    }
  },
  async deleteSkillCategory (context, skillCategory) {
    try {
      const response = await Vue.axios.post(`${backendURL}/deleteSkillCategory`, skillCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteSkillCategory', skillCategory);
    } catch (error) {
      throw error;
    }
  },
  async createSkill (context, skill) {
    try {
      const response = await Vue.axios.post(`${backendURL}/createSkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createSkill', response.data.skill);  //skillObject
    } catch (error) {
      throw error;
    }
  },
  async modifySkill (context, skill) {
    try {
      const response = await Vue.axios.post(`${backendURL}/modifySkill`, skill);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifySkill', response.data.skill);  //skillObject
    } catch (error) {
      throw error;
    }
  },
  async deleteSkill (context, skillID) {
    try {
      const response = await Vue.axios.post(`${backendURL}/deleteSkill`, skillID);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteSkill', skillID);
    } catch (error) {
      throw error;
    }
  },
};

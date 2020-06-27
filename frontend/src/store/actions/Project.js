import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async setProjectCategory (context, projectCategory) {
    try {
      const response = await Vue.axios.post(`${backendURL}/setProjectCategory`, projectCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setProjectCategory', projectCategory);
    } catch (error) {
      throw error;
    }
  },
  async deleteProjectCategory (context, projectCategory) {
    try {
      const response = await Vue.axios.post(`${backendURL}/deleteProjectCategory`, projectCategory);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteProjectCategory', projectCategory);
    } catch (error) {
      throw error;
    }
  },
  async createProject (context, project) {
    try {
      const response = await Vue.axios.post(`${backendURL}/createProject`, project);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createProject', response.data.project);  //projectObject
    } catch (error) {
      throw error;
    }
  },
  async modifyProject (context, project) {
    try {
      const response = await Vue.axios.post(`${backendURL}/modifyProject`, project);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifyProject', response.data.project);  //projectObject
    } catch (error) {
      throw error;
    }
  },
  async deleteProject (context, projectID) {
    try {
      const response = await Vue.axios.post(`${backendURL}/deleteProject`, projectID);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteProject', projectID);
    } catch (error) {
      throw error;
    }
  },
};

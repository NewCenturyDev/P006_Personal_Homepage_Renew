import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async checkSession () {
    try {
      const response = await Vue.axios.post(`${backendURL}/checkSession`, {});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      return response.data.auth;
    } catch (error) {
      throw error;
    }
  },
  async login (context, input) {
    try {
      const response = await Vue.axios.post(`${backendURL}/login`, input);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
    } catch (error) {
      throw error;
    }
  },
  async logout () {
    try {
      const response = await Vue.axios.post(`${backendURL}/logout`, {});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
    } catch (error) {
      throw error;
    }
  },
};

import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async setCodeName (context, codeName) {
    try {
      const response = await Vue.axios.post(`${backendURL}/setCodeName`, codeName);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setCodeName', codeName);
    } catch (error) {
      throw error;
    }
  },
  async setPresentation (context, presentation) {
    try {
      const response = await Vue.axios.post(`${backendURL}/setPresentation`, presentation);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setPresentation', presentation);
    } catch (error) {
      throw error;
    }
  },
  async setProfilePhoto (context, imageFile) {
    try {
      const response = await Vue.axios.post(`${backendURL}/setProfilePhoto`, imageFile);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
    } catch (error) {
      throw error;
    }
  },
};

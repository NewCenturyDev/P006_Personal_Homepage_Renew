import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async getProfile (context) {
    try {
      const response = await Vue.axios.get(`${backendURL}/getProfile`);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('loadProfile', response.data.profile);
    } catch (error) {
      throw error;
    }
  },
  async setCodename (context, codename) {
    try {
      if (codename.length === 0) {
        throw 'GitHub 코드네임을 작성해 주십시오';
      }
      const response = await Vue.axios.post(`${backendURL}/setCodename`, {codename});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setCodename', codename);
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async setPresentation (context, presentation) {
    if (presentation.length === 0) {
      throw '자기소개 내용을 작성해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/setPresentation`, {presentation});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setPresentation', presentation);
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async setProfilePhoto (context, imageFile) {
    if (imageFile === null) {
      throw '개인 프로필 이미지를 첨부해 주십시오';
    }
    const formData = new FormData();
    formData.append('file', imageFile);
    try {
      const response = await Vue.axios.post(`${backendURL}/setProfilePhoto`, formData);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('setProfilePhoto', response.data.url);
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
};

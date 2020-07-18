import Vue from 'vue';
import backendURL from '../../plugins/host';

export default {
  async getActivity (context) {
    try {
      const response = await Vue.axios.get(`${backendURL}/getActivity`);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('loadActivity', response.data.activityList);
    } catch (error) {
      throw error;
    }
  },
  async createActivity (context, activity) {
    if (activity.content.length === 0) {
      throw '활동 내용을 입력해 주십시오';
    }
    if (activity.timestamp.length === 0) {
      throw '활동 일자를 입력해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/createActivity`, activity);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('createActivity', response.data.activity);  //activityObject
      alert('추가되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async modifyActivity (context, activity) {
    if (activity.content.length === 0) {
      throw '활동 내용을 입력해 주십시오';
    }
    if (activity.timestamp.length === 0) {
      throw '활동 일자를 입력해 주십시오';
    }
    try {
      const response = await Vue.axios.post(`${backendURL}/modifyActivity`, activity);
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('modifyActivity', response.data.activity);  //activityObject
      alert('변경되었습니다.');
    } catch (error) {
      throw error;
    }
  },
  async deleteActivity (context, activityID) {
    try {
      if (typeof activityID !== 'number' || activityID < 1) {
        throw 'activity 오브젝트의 ID가 잘못되었습니다';
      }
      const response = await Vue.axios.post(`${backendURL}/deleteActivity`, {id: activityID});
      if (response.data.status.success === false) {
        throw response.data.status.message;
      }
      context.commit('deleteActivity', activityID);
      alert('삭제되었습니다.');
    } catch (error) {
      throw error;
    }
  },
};

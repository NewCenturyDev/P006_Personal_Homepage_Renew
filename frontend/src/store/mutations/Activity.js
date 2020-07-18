export default {
  loadActivity (state, activityList) {
    state.activities = activityList;
  },
  createActivity (state, activity) {
    state.activities.push(activity);
    state.activities.sort((a, b) => (a.id > b.id));
  },
  modifyActivity (state, activity) {
    const targetIndex = state.activities.findIndex((existActivity) => (existActivity.id === activity.id));
    state.activities.splice(targetIndex, 1, activity);
  },
  deleteActivity (state, activityID) {
    const targetIndex = state.activities.findIndex((existActivity) => (existActivity.id === activityID));
    state.activities.splice(targetIndex, 1);
  },
};

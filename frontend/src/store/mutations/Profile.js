export default {
  loadProfile (state, profile) {
    state.profile = profile;
  },
  setCodename (state, codename) {
    state.profile.codename = codename;
  },
  setPresentation (state, presentation) {
    state.profile.presentation = presentation;
  },
  setProfilePhoto (state, url) {
    state.profile.photo = url;
  },
};

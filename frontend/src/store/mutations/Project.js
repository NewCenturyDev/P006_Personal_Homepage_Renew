export default {
  setProjectCategory (state, projectCategory) {
    const targetIndex = state.projectCategory.indexOf(projectCategory);
    if (targetIndex === -1) {
      state.projectCategory.push(projectCategory);
      state.projectCategory.sort();
    } else {
      state.projectCategory.splice(targetIndex, 1, projectCategory);
    }
  },
  deleteProjectCategory (state, projectCategory) {
    const targetIndex = state.projectCategory.indexOf(projectCategory);
    state.projectCategory.splice(targetIndex, 1);
  },
  createProject (state, project) {
    state.projects.push(project);
    state.projects.sort((a, b) => (a.id > b.id));
  },
  modifyProject (state, project) {
    const targetIndex = state.projects.findIndex((existProject) => (existProject.id === project.id));
    state.projects.splice(targetIndex, 1, project);
  },
  deleteProject (state, projectID) {
    const targetIndex = state.projects.findIndex((existProject) => (existProject.id === projectID));
    state.projects.splice(targetIndex, 1);
  },
};

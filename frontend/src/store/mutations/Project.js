export default {
  loadProjectCategory (state, projectCategoryList) {
    state.projectCategory = projectCategoryList;
  },
  createProjectCategory (state, projectCategory) {
    state.projectCategory.push(projectCategory);
    state.projectCategory.sort((a, b) => (a.id > b.id));
  },
  modifyProjectCategory (state, projectCategory) {
    const targetIndex = state.projectCategory.findIndex((existCategory) => (existCategory.id === projectCategory.id));
    state.projectCategory.splice(targetIndex, 1, projectCategory);
  },
  deleteProjectCategory (state, projectCategoryID) {
    const targetIndex = state.projectCategory.findIndex((existCategory) => (existCategory.id === projectCategoryID));
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

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
  loadProjectList (state, projectList) {
    projectList.forEach((project) => {
      project.screenshot = JSON.parse(project.screenshot);
      project.stackTags = JSON.parse(project.tags);
      project.tags = undefined;
    });
    state.projects = projectList;
  },
  createProject (state, project) {
    project.screenshot = JSON.parse(project.screenshot);
    project.stackTags = JSON.parse(project.stackTags);
    state.projects.push(project);
    state.projects.sort((a, b) => (a.id > b.id));
  },
  modifyProject (state, project) {
    //TODO: 이상하게 모디파이에만 파일 적용안됨 (새로고침하면 괜찮음)
    project.screenshot = JSON.parse(project.screenshot);
    project.stackTags = JSON.parse(project.stackTags);
    const targetIndex = state.projects.findIndex((existProject) => (existProject.id === project.id));
    state.projects.splice(targetIndex, 1, project);
  },
  deleteProject (state, projectID) {
    const targetIndex = state.projects.findIndex((existProject) => (existProject.id === projectID));
    state.projects.splice(targetIndex, 1);
  },
};

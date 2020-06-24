export default {
  getSkillByCategory(state) {
    return (category) => {
      return state.skills.filter((skill) => (skill.category === category));
    };
  },
  getProjectByCategory(state) {
    return (category) => {
      return state.projects.filter((project) => (project.category === category));
    };
  },
};

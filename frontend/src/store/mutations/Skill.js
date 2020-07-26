export default {
  loadSkillCategory (state, skillCategoryList) {
    state.skillCategory = skillCategoryList;
  },
  createSkillCategory (state, skillCategory) {
    state.skillCategory.push(skillCategory);
    state.skillCategory.sort((a, b) => (a.id > b.id));
  },
  modifySkillCategory (state, skillCategory) {
    const targetIndex = state.skillCategory.findIndex((existCategory) => (existCategory.id === skillCategory.id));
    state.skillCategory.splice(targetIndex, 1, skillCategory);
  },
  deleteSkillCategory (state, skillCategoryID) {
    const targetIndex = state.skillCategory.findIndex((existCategory) => (existCategory.id === skillCategoryID));
    state.skillCategory.splice(targetIndex, 1);
  },
  loadSkillList (state, skillList) {
    state.skills = skillList;
  },
  createSkill (state, skill) {
    state.skills.push(skill);
    state.skills.sort((a, b) => (a.id > b.id));
  },
  modifySkill (state, skill) {
    const targetIndex = state.skills.findIndex((existSkill) => (existSkill.id === skill.id));
    state.skills.splice(targetIndex, 1, skill);
  },
  deleteSkill (state, skillID) {
    const targetIndex = state.skills.findIndex((existSkill) => (existSkill.id === skillID));
    state.skills.splice(targetIndex, 1);
  },
};

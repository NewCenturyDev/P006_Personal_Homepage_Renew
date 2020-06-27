export default {
  setSkillCategory (state, skillCategory) {
    const targetIndex = state.skillCategory.indexOf(skillCategory);
    if (targetIndex === -1) {
      state.skillCategory.push(skillCategory);
      state.skillCategory.sort();
    } else {
      state.skillCategory.splice(targetIndex, 1, skillCategory);
    }
  },
  deleteSkillCategory (state, skillCategory) {
    const targetIndex = state.skillCategory.indexOf(skillCategory);
    state.skillCategory.splice(targetIndex, 1);
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

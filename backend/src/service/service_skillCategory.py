from ..dao.dao_skillCategory import SkillCategoryDAO
from .service_crud import CrudService

class SkillCategoryService(CrudService):
  def __init__(self):
    self.dao = SkillCategoryDAO()

from ..dao.dao_projectCategory import ProjectCategoryDAO
from .service_crud import CrudService

class ProjectCategoryService(CrudService):
  def __init__(self):
    self.dao = ProjectCategoryDAO()

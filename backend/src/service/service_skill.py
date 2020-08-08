from ..dao.dao_skill import SkillDAO
from .service_crud import CrudService
from .service_file import FileService

class SkillService(CrudService):
  fileService = FileService()
  def __init__(self):
    self.dao = SkillDAO()
  def delete(self, skillID):
    try:
      self.fileService.deletePreviousFile("skill", "skill_" + str(skillID))
      self.dao.delete(skillID)
    except Exception as error:
      raise error
  def uploadSkillImage(self, fileField, skillID):
    try:
      self.fileService.checkFileIsNull(fileField)
      fileURL = self.fileService.uploadSingleFile(fileField["file"], "image", "skill", "skill_" + str(skillID))
      skill = self.dao.updateFileURL(fileURL, skillID)
      return skill
    except Exception as error:
      raise error

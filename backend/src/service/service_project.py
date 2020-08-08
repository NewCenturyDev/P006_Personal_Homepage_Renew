import simplejson as json

from ..dao.dao_project import ProjectDAO
from .service_crud import CrudService
from .service_file import FileService

class ProjectService(CrudService):
  fileService = FileService()
  def __init__(self):
    self.dao = ProjectDAO()
  def create(self, project):
    project["stackTags"] = self._convertTagStringToList(project["stackTags"])
    return self.dao.insert(project)
  def modify(self, project):
    if type(project["stackTags"]) == list:
      project["stackTags"] = json.dumps(project["stackTags"])
    else:
      project["stackTags"] = self._convertTagStringToList(project["stackTags"])
    return self.dao.update(project)
  def delete(self, projectID):
    try:
      self.fileService.deletePreviousDir("project", projectID)
      self.dao.delete(projectID)
    except Exception as error:
      raise error
  def uploadProjectImageList(self, fileField, projectID):
    try:
      self.fileService.checkFileIsNull(fileField)
      print(fileField.getlist("file"))
      fileURLList = self.fileService.uploadMultipleFiles(fileField.getlist("file"), "image", "project", projectID, "project_screenshot_")
      return self.dao.updateFileURLList(fileURLList, projectID)
    except Exception as error:
      raise error
  def _convertTagStringToList(self, tagString):
    # 쉼표로 구분된 게시물 태그를 공백 무시하고 쉼표 기준으로 리스트로 변환
    return json.dumps(tagString.replace(" ", "").split(","))

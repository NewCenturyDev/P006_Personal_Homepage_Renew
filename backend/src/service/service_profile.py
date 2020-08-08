from ..dao.dao_profile import ProfileDAO
from .service_file import FileService

profileDAO = ProfileDAO()
fileService = FileService()
class ProfileService():
  def getProfile(self):
    try:
      profile = profileDAO.getProfile()
      return profile
    except Exception as error:
      raise error
  def setCodename(self, codename):
    try:
      profileDAO.updateCodename(codename)
    except Exception as error:
      raise error
  def setPresentation(self, presentation):
    try:
      profileDAO.updatePresentation(presentation)
    except Exception as error:
      raise error
  def setProfilePhoto(self, profilePhoto):
    if profilePhoto.filename == "":
      raise Exception("파일이 선택되지 않았습니다")
      return
    try:
      fileURL = fileService.uploadSingleFile(profilePhoto, "image", "profile", "profilePhoto")
      profileDAO.updateProfilePhoto(fileURL)
      return fileURL
    except Exception as error:
      raise error

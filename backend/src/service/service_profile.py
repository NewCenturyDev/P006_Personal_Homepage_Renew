from dao.dao_profile import ProfileDAO
from service.service_file import FileService

profileDAO = ProfileDAO()
fileService = FileService()
class ProfileService():
  def getProfile():
    try:
      profile = profileDAO.getProfile()
      return profile
    except Exception as error:
      raise error
  def setCodename(codename):
    try:
      profileDAO.updateCodename()
    except Exception as error:
      raise error
  def setPresentation(presentation):
    try:
      profileDAO.updatePresentation()
    except Exception as error:
      raise error
  def setProfilePhoto(profilePhoto):
    if profilePhoto.filename == "":
      raise "파일이 선택되지 않았습니다"
      return
    try:
      fileURL = fileService.uploadSingleFile(profilePhoto, "profile", "profilePhoto")
      profileDAO.updateProfilePhoto(fileURL)
      return fileURL
    except Exception as error:
      raise error

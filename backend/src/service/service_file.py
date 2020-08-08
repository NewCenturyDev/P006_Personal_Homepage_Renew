import os
import glob

#import Application Root Path
from flask import current_app

class FileService():
  ALLOWED_EXTENSIONS = {
    "document": {"txt", "pdf", "md", "docx", "pptx", "xlsx"},
    "image": {"png", "jpg", "jpeg", "gif", "bmp"},
    "audio": {"mp3", "flac", "wav", "ogg", "webm"},
    "video": {"mp4", "webm"},
  }
  def uploadSingleFile(self, file, fileType, fileCategory, fileName):
    if (self._isAllowedFile(file.filename, fileType)):
      self._checkDataRootDir()
      self._checkDataCategoryDir(fileCategory)
      self.deletePreviousFile(fileCategory, fileName)
      file.save(os.path.join(current_app.root_path, "view", "data", fileCategory, fileName + self._getExtension(file.filename)))
      fileURL = "data/" + fileCategory + "/" + fileName + self._getExtension(file.filename)
      return fileURL
    else:
      raise Exception("허용되지 않는 형식의 파일입니다")
  def uploadMultipleFiles(self, fileList, fileType, fileCategory, entityID, fileName):
    self._checkDataRootDir()
    self._checkDataCategoryDir(fileCategory)
    self._checkDataEntityDir(fileCategory, entityID)
    self.deletePreviousDir(fileCategory, entityID)
    fileCount = 0
    fileURLList = []
    for targetFile in fileList:
      if targetFile and self._isAllowedFile(targetFile.filename, fileType) == False:
        continue
      fileCount += 1
      targetFile.save(os.path.join(current_app.root_path, "view", "data", fileCategory, entityID, fileName + str(fileCount) + self._getExtension(targetFile.filename)))
      fileURLList.append("data/" + fileCategory + "/" + entityID + "/" + fileName + str(fileCount) + self._getExtension(targetFile.filename))
    return fileURLList
  def deletePreviousFile(self, fileCategory, fileName):
    # Delete previous image file
    previousFileList = glob.glob(os.path.join(current_app.root_path, "view", "data", fileCategory, fileName + ".*"))
    for targetFile in previousFileList:
      os.remove(os.path.join(current_app.root_path, "view", "data", fileCategory, targetFile))
  def deletePreviousDir(self, fileCategory, entityID):
    # Delete previous image file
    previousFileList = glob.glob(os.path.join(current_app.root_path, "view", "data", fileCategory, str(entityID), "*.*"))
    for targetFile in previousFileList:
      if os.path.exists(os.path.join(current_app.root_path, "view", "data", fileCategory, str(entityID), targetFile)):
        os.remove(os.path.join(current_app.root_path, "view", "data", fileCategory, str(entityID), targetFile))
  def checkFileIsNull(self, requestFiles):
    if "file" not in requestFiles:
      raise Exception("폼데이터에 파일이 없습니다")
  def _isAllowedFile(self, filename, rule):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in self.ALLOWED_EXTENSIONS[rule]
  def _getExtension(self, filename):
    return "." + filename.rsplit(".", 1)[1].lower()
  def _checkDataRootDir(self):
    # Create directory if not exist
    if not os.path.isdir(os.path.join(current_app.root_path, "view", "data")):
      os.mkdir(os.path.join(current_app.root_path, "view", "data"))
  def _checkDataCategoryDir(self, fileCategory):
    # Create directory if not exist
    if not os.path.isdir(os.path.join(current_app.root_path, "view", "data", fileCategory)):
      os.mkdir(os.path.join(current_app.root_path, "view", "data", fileCategory))
  def _checkDataEntityDir(self, fileCategory, entityID):
    # Create directory if not exist
    if not os.path.isdir(os.path.join(current_app.root_path, "view", "data", fileCategory, entityID)):
      os.mkdir(os.path.join(current_app.root_path, "view", "data", fileCategory, entityID))

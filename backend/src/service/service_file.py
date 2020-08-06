class FileService():
  ALLOWED_EXTENSIONS = {
    "document": {"txt", "pdf", "md", "docx", "pptx", "xlsx"},
    "image": {"png", "jpg", "jpeg", "gif", "bmp"},
    "audio": {"mp3", "flac", "wav", "ogg", "webm"},
    "video": {"mp4", "webm"},
  }
  def uploadSingleFile(file, fileCategory, fileName):
    # Create directory if not exist
    if (self._isAllowedFile(file.filename, "image")):
      self._checkDataRootDir()
      self._checkDataCategoryDir(fileCategory)
      self._deletePreviousFile(fileCategory, fileName)
      file.save(os.path.join(app.root_path, "view", "data", fileCategory, fileName + _getExtension(file.filename)))
      fileURL = "data/" + fileCategory + "/" + fileName + _getExtension(file.filename)
      return fileURL
    else:
      raise "허용되지 않는 형식의 파일입니다"
  def uploadMultipleFiles():

  def _isAllowedFile(filename, rule):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS[rule]
  def _getExtension(filename):
    return "." + filename.rsplit(".", 1)[1].lower()
  def _checkDataRootDir():
    if not os.path.isdir(os.path.join(app.root_path, "view", "data")):
      os.mkdir(os.path.join(app.root_path, "view", "data"))
  def _checkDataCategoryDir(fileCategory):
    if not os.path.isdir(os.path.join(app.root_path, "view", "data", fileCategory)):
      os.mkdir(os.path.join(app.root_path, "view", "data", fileCategory))
  def _deletePreviousFile(fileCategory, fileName)
    # Delete previous image file
    previousFileList = glob.glob(os.path.join(app.root_path, "view", "data", fileCategory, fileName + ".*"))
    for targetFile in previousFileList:
      os.remove(os.path.join(app.root_path, "view", "data", fileCategory, targetFile))

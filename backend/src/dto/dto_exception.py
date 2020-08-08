class ExceptionDTO():
  message = None
  dto = {
    "status": {
      "success": False,
      "message": message,
    }
  }
  def __init__(self, error):
    print(error)
    self.message = error.args[0]
  def getDTO(self):
    return self.dto

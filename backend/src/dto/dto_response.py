class ResponseDTO():
  message = None
  dto = {
    "status": {
      "success": True,
      "message": self.message,
    }
  }
  def __init__(self, message):
    self.message = message
  def getDTO(self):
    return self.dto

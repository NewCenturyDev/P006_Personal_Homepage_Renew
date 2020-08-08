from ..dao.dao_activity import ActivityDAO

activityDAO = ActivityDAO()
class ActivityService():
  def getActivity(self):
    try:
      return activityDAO.getActivity()
    except Exception as error:
      raise error
  def createActivity(self, activity):
    try:
      return activityDAO.insertActivity(activity)
    except Exception as error:
      raise error
  def modifyActivity(self, activity):
    try:
      return activityDAO.updateActivity(activity)
    except Exception as error:
      raise error
  def deleteActivity(self, activityID):
    try:
      return activityDAO.deleteActivity(activityID)
    except Exception as error:
      raise error

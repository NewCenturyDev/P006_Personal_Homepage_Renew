import simplejson as json
from ..db import db, DICT_CURSOR

class ActivityDAO():
  def getActivity(self):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM activity")
      activityList = dictCursor.fetchall()
      json.dumps( [dict(ix) for ix in activityList] )
      return activityList
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
  def insertActivity(self, activity):
    cursor = db.cursor()
    try:
      cursor.execute("INSERT INTO activity (content, timestamp) VALUE (%s, %s)", (activity["content"], activity["timestamp"]))
      db.commit()
      cursor.execute("SELECT * FROM activity WHERE content = %s AND timestamp = %s", (activity["content"], activity["timestamp"]))
      activity = cursor.fetchone()
      return activity
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def updateActivity(self, activity):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE activity SET content = %s, timestamp = %s WHERE id = %s", (activity["content"], activity["timestamp"], activity["id"]))
      db.commit()
      cursor.execute("SELECT * FROM activity WHERE id = %s", (activity["id"]))
      activity = cursor.fetchone()
      return activity
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def deleteActivity(self, activityID):
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM activity WHERE id = %s", (activityID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()

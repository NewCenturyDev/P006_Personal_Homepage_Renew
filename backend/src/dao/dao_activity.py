import simplejson as json
import pymysql

class ActivityDAO():
  def getActivity(self):
    try:
      cursor = db.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT * FROM activity")
      activityList = cursor.fetchall()
      json.dumps( [dict(ix) for ix in activityList] )
      return activityList
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def insertActivity(self, activity):
    try:
      cursor = db.cursor()
      cursor.execute("INSERT INTO activity (content, timestamp) VALUE (%s, %s)", (activity["content"], activity["timestamp"]))
      db.commit()
      cursor.execute("SELECT * FROM activity WHERE content = %s AND timestamp = %s", (activity["content"], activity["timestamp"]))
      activity = cursor.fetchone()
      return activity
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def updateActivity(self, activity):
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE activity SET content = %s, timestamp = %s WHERE id = %s", (activity["content"], activity["timestamp"], activity["id"]))
      db.commit()
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def deleteActivity(self, activityID):
    try:
      cursor = db.cursor()
      cursor.execute("DELETE FROM activity WHERE id = %s", (activityID))
      db.commit()
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()

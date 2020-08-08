from ..db import db, DICT_CURSOR

class ProfileDAO():
  def getProfile(self):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM profile WHERE id = 1")
      profile = dictCursor.fetchone()
      return profile
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
  def updateCodename(self, codename):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE profile SET codename = %s WHERE id = 1", (codename))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def updatePresentation(self, presentation):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE profile SET presentation = %s WHERE id = 1", (presentation))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def updateProfilePhoto(self, fileURL):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE profile SET photo = %s WHERE id = 1", (fileURL))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()

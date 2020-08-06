from config import db

class ProfileDAO():
  def getProfile():
    try:
      cursor = db.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT * FROM profile WHERE id = 1")
      profile = cursor.fetchone()
      return profile
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def updateCodename(codename):
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE profile SET codename = %s WHERE id = 1", (codename))
      db.commit()
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def updatePresentation(presentation):
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE profile SET presentation = %s WHERE id = 1", (presentation))
      db.commit()
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()
  def updateProfilePhoto(fileURL):
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE profile SET photo = %s WHERE id = 1", (fileURL))
      db.commit()
    except Exception as error:
      print(error)
      raise "데이터베이스에 오류가 발생했습니다"
    finally:
      cursor.close()

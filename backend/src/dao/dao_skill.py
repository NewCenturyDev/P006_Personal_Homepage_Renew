import simplejson as json
from ..db import db, DICT_CURSOR

class SkillDAO():
  def select(self):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM skill")
      skillList = dictCursor.fetchall()
      json.dumps( [dict(ix) for ix in skillList] )
      return skillList
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
  def insert(self, skill):
    cursor = db.cursor()
    try:
      cursor.execute("INSERT INTO skill (name, category) VALUE (%s, %s)", (skill["name"], skill["category"]))
      db.commit()
      cursor.execute("SELECT id FROM skill WHERE name = %s", (skill["name"]))
      skillID = cursor.fetchone()
      return skillID
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def update(self, skill):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE skill SET name = %s, category = %s WHERE id = %s", (skill["name"], skill["category"], skill["id"]))
      db.commit()
      cursor.execute("SELECT * FROM skill WHERE id = %s", skill["id"])
      skill = cursor.fetchone()
      return skill
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def delete(self, skillID):
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM skill WHERE id = %s", (skillID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def updateFileURL(self, fileURL, skillID):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE skill SET image = %s WHERE id = %s", (fileURL, skillID))
      db.commit()
      cursor.execute("SELECT * FROM skill WHERE id = %s", skillID)
      skill = cursor.fetchone()
      return skill
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()

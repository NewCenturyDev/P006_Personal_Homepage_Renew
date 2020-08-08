import simplejson as json
from ..db import db, DICT_CURSOR

class SkillCategoryDAO():
  def select(self):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM skillcategory ORDER BY id")
      skillCategoryList = dictCursor.fetchall()
      json.dumps( [dict(ix) for ix in skillCategoryList] )
      return skillCategoryList
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
  def insert(self, skillCategory):
    cursor = db.cursor()
    try:
      cursor.execute("INSERT INTO skillCategory (category) VALUE (%s)", (skillCategory["category"]))
      db.commit()
      cursor.execute("SELECT * FROM skillCategory WHERE category = %s", (skillCategory["category"]))
      skillCategory = cursor.fetchone()
      return skillCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def update(self, skillCategory):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE skillCategory SET category = %s WHERE id = %s", (skillCategory["category"], skillCategory["id"]))
      db.commit()
      cursor.execute("SELECT * FROM skillCategory WHERE category = %s", (skillCategory["category"]))
      skillCategory = cursor.fetchone()
      return skillCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def delete(self, skillCategoryID):
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM skillCategory WHERE id = %s", (skillCategoryID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()

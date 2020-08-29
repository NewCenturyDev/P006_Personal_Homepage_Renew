import simplejson as json
from ..db import get_DB_connection, DICT_CURSOR

class SkillCategoryDAO():
  def select(self):
    db = get_DB_connection()
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
      db.close()
  def insert(self, skillCategory):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("INSERT INTO skillcategory (category) VALUE (%s)", (skillCategory["category"]))
      db.commit()
      cursor.execute("SELECT * FROM skillcategory WHERE category = %s", (skillCategory["category"]))
      skillCategory = cursor.fetchone()
      return skillCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()
  def update(self, skillCategory):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE skillcategory SET category = %s WHERE id = %s", (skillCategory["category"], skillCategory["id"]))
      db.commit()
      cursor.execute("SELECT * FROM skillcategory WHERE category = %s", (skillCategory["category"]))
      skillCategory = cursor.fetchone()
      return skillCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()
  def delete(self, skillCategoryID):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM skillcategory WHERE id = %s", (skillCategoryID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()

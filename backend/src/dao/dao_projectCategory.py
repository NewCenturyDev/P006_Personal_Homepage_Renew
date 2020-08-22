import simplejson as json
from ..db import db, DICT_CURSOR

class ProjectCategoryDAO():
  def select(self):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM projectcategory ORDER BY id")
      projectCategoryList = dictCursor.fetchall()
      json.dumps( [dict(ix) for ix in projectCategoryList] )
      return projectCategoryList
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
  def insert(self, projectCategory):
    cursor = db.cursor()
    try:
      cursor.execute("INSERT INTO projectcategory (category) VALUE (%s)", (projectCategory["category"]))
      db.commit()
      cursor.execute("SELECT * FROM projectcategory WHERE category = %s", (projectCategory["category"]))
      projectCategory = cursor.fetchone()
      return projectCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def update(self, projectCategory):
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE projectcategory SET category = %s WHERE id = %s", (projectCategory["category"], projectCategory["id"]))
      db.commit()
      cursor.execute("SELECT * FROM projectcategory WHERE category = %s", (projectCategory["category"]))
      projectCategory = cursor.fetchone()
      return projectCategory
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
  def delete(self, projectCategoryID):
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM projectcategory WHERE id = %s", (projectCategoryID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()

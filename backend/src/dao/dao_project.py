import simplejson as json
from ..db import get_DB_connection, DICT_CURSOR

class ProjectDAO():
  def select(self):
    db = get_DB_connection()
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM project ORDER BY id")
      projectList = dictCursor.fetchall()
      json.dumps( [dict(ix) for ix in projectList] )
      return projectList
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      dictCursor.close()
      db.close()
  def insert(self, project):
    db = get_DB_connection()
    cursor = db.cursor()
    print(project["stackTags"])
    try:
      cursor.execute("INSERT INTO project (name, category, link, discription, content, tags) VALUE (%s, %s, %s, %s, %s, %s)", (project["name"], project["category"], project["link"], project["discription"], project["content"], project["stackTags"]))
      db.commit()
      cursor.execute("SELECT id FROM project WHERE name = %s", (project["name"]))
      projectID = cursor.fetchone()
      return projectID
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()
  def update(self, project):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE project SET name = %s, category = %s, link = %s, discription = %s, content = %s, tags = %s WHERE id = %s", (project["name"], project["category"], project["link"], project["discription"], project["content"], project["stackTags"], project["id"]))
      db.commit()
      cursor.execute("SELECT * FROM project WHERE id = %s", project["id"])
      project = cursor.fetchone()
      return project
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()
  def delete(self, projectID):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("DELETE FROM project WHERE id = %s", (projectID))
      db.commit()
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()
  def updateFileURLList(self, FileURLList, projectID):
    db = get_DB_connection()
    cursor = db.cursor()
    try:
      cursor.execute("UPDATE project SET screenshot = %s WHERE id = %s", (json.dumps(FileURLList), projectID))
      db.commit()
      cursor.execute("SELECT * FROM project WHERE id = %s", projectID)
      project = cursor.fetchone()
      return project
    except Exception as error:
      print(error)
      raise Exception("데이터베이스에 오류가 발생했습니다")
    finally:
      cursor.close()
      db.close()

from ..db import get_DB_connection, DICT_CURSOR

class AuthDAO():
  def getAccount(self, username, password):
    db = get_DB_connection()
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
      account = dictCursor.fetchone()
      return account
    except Exception as error:
      raise error
    finally:
      dictCursor.close()
      db.close()

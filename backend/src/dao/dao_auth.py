from ..db import db, DICT_CURSOR

class AuthDAO():
  def getAccount(self, username, password):
    dictCursor = db.cursor(DICT_CURSOR)
    try:
      dictCursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
      account = dictCursor.fetchone()
      return account
    except Exception as error:
      raise error
    finally:
      dictCursor.close()

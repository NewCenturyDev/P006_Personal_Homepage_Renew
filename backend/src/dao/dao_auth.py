class AuthDAO():
  def getAccount(username, password):
    try:
      cursor = db.cursor(pymysql.cursors.DictCursor)
      cursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
      account = cursor.fetchone()
      return account
    except Exception as error:
      raise error
    finally:
      cursor.close()

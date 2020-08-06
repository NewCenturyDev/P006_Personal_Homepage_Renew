from dao.dao_auth import AuthDAO
from flask import session

authDAO = AuthDAO()

class AuthService():
  def processLogin(username, password):
    try:
      account = authDAO.getAccount(username, password)
    except Exception as error:
      raise error
    result = self._activateSession(account)
    return result
  def checkSession():
    return session["loggedIn"] == True
  def processLogout():
    session.clear()
  def _activateSession(account):
    if account:
      session["loggedIn"] = True
      session["id"] = account["id"]
      session["username"] = account["username"]
      session["permission"] = account["permission"]
      return True
    else
      return False

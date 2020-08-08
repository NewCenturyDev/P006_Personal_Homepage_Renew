from ..dao.dao_auth import AuthDAO
from flask import session

authDAO = AuthDAO()

class AuthService():
  def processLogin(self, username, password):
    try:
      account = authDAO.getAccount(username, password)
      self._activateSession(account)
    except Exception as error:
      raise error
  def checkSession(self):
    if (session and session["loggedIn"] == True):
      return
    else:
      raise Exception("로그인이 되어 있지 않습니다")
  def processLogout(self):
    session.clear()
  def _activateSession(self, account):
    if account:
      session["loggedIn"] = True
      session["id"] = account["id"]
      session["username"] = account["username"]
      session["permission"] = account["permission"]
    else:
      raise Exception("로그인이 되어 있지 않습니다")

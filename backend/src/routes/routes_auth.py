from flask import Blueprint, render_template, request, redirect, jsonify, url_for

#import service
from service.service_auth import AuthService

authService = AuthService()
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route("/")
def home():
  return render_template("index.html")

@auth.route("/login", methods=["POST"])
def login():
  if not request.is_json:
    return "Please request by JSON", 400

  username = request.json.get("username", None)
  password = request.json.get("password", None)

  try:
    loginResult = authService.processLogin(username, password)
  except Exception as error:
    print(error)
    return jsonify({
        "status": {
          "success": False,
          "message": "데이터베이스에 오류가 발생했습니다",
        }
      }), 200
  if (loginResult):
    return jsonify({
      "status": {
      "success": True,
      "message": "로그인 되었습니다",
    }}), 200
  else:
    return jsonify({
      "status": {
        "success": False,
        "message": "ID 또는 비밀번호를 다시 확인해 주십시오",
      }
    }), 200

@auth.route("/checkSession", methods=["POST"])
def checkSession():
  if not request.is_json:
    return "Please request by JSON", 400

  if authService.checkSession():
    return jsonify({
      "status": {
        "success": True,
        "message": "로그인이 되어 있습니다",
      },
      "auth": True,
    }), 200
  else:
    return jsonify({
      "status": {
        "success": True,
        "message": "로그인이 되어 있지 않습니다",
      },
      "auth": False,
    }), 200

@auth.route("/logout", methods=["POST"])
def logout():
  if not request.is_json:
    return "Please request by JSON", 400

  authService.processLogout()
  return jsonify({
    "status": {
      "success": True,
      "message": "로그아웃 되었습니다",
    }
  }), 200

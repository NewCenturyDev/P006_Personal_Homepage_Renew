from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import simplejson as json

#import service
from ..service.service_auth import AuthService

#import DTO
from ..dto.dto_exception import ExceptionDTO

authService = AuthService()
authBluePrint = Blueprint('auth', __name__, template_folder='templates')

@authBluePrint.route("/login", methods=["POST"])
def login():
  if not request.is_json:
    return "Please request by JSON", 400

  username = request.json.get("username", None)
  password = request.json.get("password", None)

  try:
    authService.processLogin(username, password)
    return jsonify({
      "status": {
        "success": True,
        "message": "로그인 되었습니다",
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

@authBluePrint.route("/checkSession", methods=["POST"])
def checkSession():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    authService.checkSession()
    return jsonify({
      "status": {
        "success": True,
        "message": "로그인이 되어 있습니다",
      },
      "auth": True,
    }), 200
  except Exception as error:
    return jsonify({
      "status": {
        "success": True,
        "message": str(error),
      },
      "auth": False,
    }), 200

@authBluePrint.route("/logout", methods=["POST"])
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

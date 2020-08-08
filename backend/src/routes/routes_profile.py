from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import simplejson as json

#import service
from ..service.service_profile import ProfileService

#import DTO
from ..dto.dto_exception import ExceptionDTO

profileService = ProfileService()
profileBluePrint = Blueprint("profile", __name__, template_folder="templates")

@profileBluePrint.route("/getProfile", methods=["GET"])
def getProfile():
  try:
    profile = profileService.getProfile()
    return jsonify({
      "status": {
        "success": True,
        "message": "프로필 조회 성공",
      },
      "profile": {
        "photo": profile["photo"],
        "codename": profile["codename"],
        "presentation": profile["presentation"]
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200
@profileBluePrint.route("/setCodename", methods=["POST"])
def setCodename():
  if not request.is_json:
    return "Please request by JSON", 400
  codename = request.json.get("codename", None)
  try:
    profileService.setCodename(codename)
    return jsonify({
      "status": {
        "success": True,
        "message": "Github 코드네임이 변경 되었습니다",
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200
@profileBluePrint.route("/setPresentation", methods=["POST"])
def setPresentation():
  if not request.is_json:
    return "Please request by JSON", 400
  presentation = request.json.get("presentation", None)
  try:
    profileService.setPresentation(presentation)
    return jsonify({
      "status": {
        "success": True,
        "message": "자기소개 메시지가 변경 되었습니다",
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200
@profileBluePrint.route("/setProfilePhoto", methods=["POST"])
def setProfilePhoto():
  if "file" not in request.files:
    return jsonify({
      "status": {
        "success": False,
        "message": "폼데이터에 파일이 없습니다",
      }
    }), 200
  try:
    fileURL = profileService.setProfilePhoto(request.files["file"])
    return jsonify({
      "status": {
        "success": True,
        "message": "프로필 사진이 변경 되었습니다",
      },
      "url": fileURL
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

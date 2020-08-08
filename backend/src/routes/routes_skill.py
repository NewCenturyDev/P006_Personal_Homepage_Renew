from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import simplejson as json

#import service
from ..service.service_skillCategory import SkillCategoryService
from ..service.service_skill import SkillService

#import DTO
from ..dto.dto_exception import ExceptionDTO

skillService = SkillService()
skillCategoryService = SkillCategoryService()
skillBluePrint = Blueprint("skill", __name__, template_folder="templates")

@skillBluePrint.route("/getSkillCategory", methods=["GET"])
def getSkillCategory():
  try:
    skillCategoryList = skillCategoryService.getList()
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리 조회 성공",
      },
      "skillCategoryList": skillCategoryList
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/createSkillCategory", methods=["POST"])
def createSkillCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skillCategory = skillCategoryService.create(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 추가 되었습니다",
      },
      "skillCategory": {
        "id": skillCategory[0],
        "category": skillCategory[1]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/modifySkillCategory", methods=["POST"])
def modifySkillCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skillCategory = skillCategoryService.modify(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 수정 되었습니다",
      },
      "skillCategory": {
        "id": skillCategory[0],
        "category": skillCategory[1]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/deleteSkillCategory", methods=["POST"])
def deleteSkillCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skillCategoryService.delete(request.json.get("id", None))
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 삭제 되었습니다",
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/getSkillList", methods=["GET"])
def getSkillList():
  try:
    skillList = skillService.getList()
    return jsonify({
      "status": {
        "success": True,
        "message": "기술스택 조회 성공",
      },
      "skillList": skillList
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/createSkill", methods=["POST"])
def createSkill():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skillID = skillService.create(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "기술스택이 추가 되었습니다, 파일을 업로드하세요",
      },
      "skillID": skillID
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200
  

@skillBluePrint.route("/modifySkill", methods=["POST"])
def modifySkill():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skill = skillService.modify(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "기술스택이 수정 되었습니다",
      },
      "skill": {
        "id": skill[0],
        "name": skill[1],
        "category": skill[2],
        "image": skill[3]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200
  

@skillBluePrint.route("/deleteSkill", methods=["POST"])
def deleteSkill():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    skillID = skillService.delete(request.json.get("id", None))
    return jsonify({
      "status": {
        "success": True,
        "message": "기술스택이 삭제 되었습니다",
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@skillBluePrint.route("/uploadSkillImage", methods=["POST"])
def uploadSkillImage():
  try:
    skill = skillService.uploadSkillImage(request.files, request.form["skillID"])
    return jsonify({
      "status": {
        "success": True,
        "message": "기술스택 이미지가 업로드 되었습니다",
      },
      "skill": {
        "id": skill[0],
        "name": skill[1],
        "category": skill[2],
        "image": skill[3]
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import simplejson as json

#import service
from ..service.service_projectCategory import ProjectCategoryService
from ..service.service_project import ProjectService

#import DTO
from ..dto.dto_exception import ExceptionDTO

projectService = ProjectService()
projectCategoryService = ProjectCategoryService()
projectBluePrint = Blueprint("project", __name__, template_folder="templates")


@projectBluePrint.route("/getProjectCategory", methods=["GET"])
def getProjectCategory():
  try:
    projectCategoryList = projectCategoryService.getList()
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리 조회 성공",
      },
      "projectCategoryList": projectCategoryList
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/createProjectCategory", methods=["POST"])
def createProjectCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    projectCategory = projectCategoryService.create(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 추가 되었습니다",
      },
      "projectCategory": {
        "id": projectCategory[0],
        "category": projectCategory[1]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/modifyProjectCategory", methods=["POST"])
def modifyProjectCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    projectCategory = projectCategoryService.modify(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 수정 되었습니다",
      },
      "projectCategory": {
        "id": projectCategory[0],
        "category": projectCategory[1]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/deleteProjectCategory", methods=["POST"])
def deleteProjectCategory():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    projectCategoryService.delete(request.json.get("id", None))
    return jsonify({
      "status": {
        "success": True,
        "message": "카테고리가 삭제 되었습니다",
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/getProjectList", methods=["GET"])
def getProjectList():
  try:
    projectList = projectService.getList()
    return jsonify({
      "status": {
        "success": True,
        "message": "프로젝트 조회 성공",
      },
      "projectList": projectList
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/createProject", methods=["POST"])
def createProject():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    projectID = projectService.create(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "프로젝트 상세정보가 추가 되었습니다, 파일을 업로드하세요",
      },
      "projectID": projectID
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/modifyProject", methods=["POST"])
def modifyProject():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    project = projectService.modify(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "프로젝트 상세정보가 변경 되었습니다",
      },
      "project": {
        "id": project[0],
        "name": project[1],
        "category": project[2],
        "link": project[3],
        "discription": project[4],
        "content": project[5],
        "screenshot": project[6],
        "stackTags": project[7]
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/deleteProject", methods=["POST"])
def deleteProject():
  if not request.is_json:
    return "Please request by JSON", 400

  try:
    projectService.delete(request.json.get("id", None))
    return jsonify({
      "status": {
        "success": True,
        "message": "프로젝트 상세정보가 삭제 되었습니다",
      }
    }), 200
  except Exception as error:
    print(error)
    return jsonify(ExceptionDTO(error).getDTO()), 200

@projectBluePrint.route("/uploadProjectScreenshotImage", methods=["POST"])
def uploadProjectScreenshotImage():
  try:
    project = projectService.uploadProjectImageList(request.files, request.form["projectID"])
    return jsonify({
      "status": {
        "success": True,
        "message": "프로젝트 상세정보가 변경 되었습니다",
      },
      "project": {
        "id": project[0],
        "name": project[1],
        "category": project[2],
        "link": project[3],
        "discription": project[4],
        "content": project[5],
        "screenshot": project[6],
        "stackTags": project[7]
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

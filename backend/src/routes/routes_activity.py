from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import simplejson as json

#import service
from ..service.service_activity import ActivityService

#import DTO
from ..dto.dto_exception import ExceptionDTO

activityService = ActivityService()
activityBluePrint = Blueprint("activity", __name__, template_folder="templates")

@activityBluePrint.route("/getActivity", methods=["GET"])
def getActivity():
  try:
    activityList = activityService.getActivity()
    return jsonify({
      "status": {
        "success": True,
        "message": "활동이력 조회 성공",
      },
      "activityList": activityList
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

@activityBluePrint.route("/createActivity", methods=["POST"])
def createActivity():
  if not request.is_json:
    return "Please request by JSON", 400

  activity = request.json
  try:
    activity = activityService.createActivity(activity)
    return jsonify({
      "status": {
        "success": True,
        "message": "활동이력이 추가 되었습니다",
      },
      "activity": {
        "id": activity[0],
        "content": activity[1],
        "timestamp": activity[2]
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

@activityBluePrint.route("/modifyActivity", methods=["POST"])
def modifyActivity():
  if not request.is_json:
    return "Please request by JSON", 400

  activity = request.json
  try:
    activity = activityService.modifyActivity(request.json)
    return jsonify({
      "status": {
        "success": True,
        "message": "활동이력이 수정 되었습니다",
      },
      "activity": {
        "id": activity[0],
        "content": activity[1],
        "timestamp": activity[2]
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

@activityBluePrint.route("/deleteActivity", methods=["POST"])
def deleteActivity():
  if not request.is_json:
    return "Please request by JSON", 400

  activityID = request.json.get("id", None)
  try:
    activityID = activityService.deleteActivity(activityID)
    return jsonify({
      "status": {
        "success": True,
        "message": "활동이력이 삭제 되었습니다",
      }
    }), 200
  except Exception as error:
    return jsonify(ExceptionDTO(error).getDTO()), 200

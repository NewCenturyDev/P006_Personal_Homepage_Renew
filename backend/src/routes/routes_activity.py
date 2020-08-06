from flask import Blueprint, render_template, request, redirect, jsonify, url_for

#import service
from service.service_activity import ActivityService

activityService = ActivityService()
activity = Blueprint("activity", __name__, template_folder="templates")

@activity.route("/getActivity", methods=["GET"])
def getActivity():
  if not request.is_json:
    return "Please request by JSON", 400

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
    return jsonify({
      "status": {
        "success": False,
        "message": error,
      }
    }), 200

@activity.route("/createActivity", methods=["POST"])
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
    return jsonify({
      "status": {
        "success": False,
        "message": error,
      }
    }), 200

@activity.route("/modifyActivity", methods=["POST"])
def modifyActivity():
  if not request.is_json:
    return "Please request by JSON", 400

  activity = request.json
  try:
    activity = activityService.modifyActivity(activity)
    return jsonify({
      "status": {
        "success": True,
        "message": "활동이력이 수정 되었습니다",
      },
      "activity": activity
    }), 200
  except Exception as error:
    return jsonify({
      "status": {
        "success": False,
        "message": error,
      }
    }), 200

@activity.route("/deleteActivity", methods=["POST"])
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
    return jsonify({
      "status": {
        "success": False,
        "message": error,
      }
    }), 200

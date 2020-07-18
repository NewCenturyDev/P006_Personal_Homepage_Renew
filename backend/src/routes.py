from flask import render_template, request, redirect, jsonify, url_for, session
from . import app
import simplejson as json

# DB
import pymysql
db = pymysql.connect(
  host="localhost",
  port=3306,
  user="page",
  passwd="page",
  db="page",
  charset="utf8"
)

# cors
from flask_cors import CORS, cross_origin
CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})

# file
import os
import glob
ALLOWED_EXTENSIONS = {
  "document": {"txt", "pdf", "md", "docx", "pptx", "xlsx"},
  "image": {"png", "jpg", "jpeg", "gif", "bmp"},
  "audio": {"mp3", "flac", "wav", "ogg", "webm"},
  "video": {"mp4", "webm"},
}
def isAllowedFile(filename, rule):
  return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS[rule]
def getExtension(filename):
  return "." + filename.rsplit(".", 1)[1].lower()

# route
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
  if not request.is_json:
    return "Please request by JSON", 400
  
  username = request.json.get("username", None)
  password = request.json.get("password", None)
  
  try:
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
    account = cursor.fetchone()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  if account:
    session["loggedIn"] = True
    session["id"] = account["id"]
    session["username"] = account["username"]
    session["permission"] = account["permission"]
    return jsonify({
      "status": {
      "success": True,
      "message": "로그인 되었습니다",
    }}), 200

  return jsonify({
    "status": {
      "success": False,
      "message": "ID 또는 비밀번호를 다시 확인해 주십시오",
    }
  }), 200

@app.route("/checkSession", methods=["POST"])
def checkSession():
  if not request.is_json:
    return "Please request by JSON", 400

  if session:
    if session["loggedIn"] == True:
      return jsonify({
        "status": {
          "success": True,
          "message": "로그인이 되어 있습니다",
        },
        "auth": True,
      }), 200

  return jsonify({
    "status": {
      "success": True,
      "message": "로그인이 되어 있지 않습니다",
    },
    "auth": False,
  }), 200

@app.route("/logout", methods=["POST"])
def logout():
  if not request.is_json:
    return "Please request by JSON", 400
  session.clear()
  return jsonify({
    "status": {
      "success": True,
      "message": "로그아웃 되었습니다",
    }
  }), 200

@app.route("/getProfile", methods=["GET"])
def getProfile():
  try:
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM profile WHERE id = 1")
    profile = cursor.fetchone()
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

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

@app.route("/setCodename", methods=["POST"])
def setCodename():
  if not request.is_json:
    return "Please request by JSON", 400
  
  codename = request.json.get("codename", None)

  try:
    cursor = db.cursor()
    cursor.execute("UPDATE profile SET codename = %s WHERE id = 1", (codename))
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  return jsonify({
    "status": {
      "success": True,
      "message": "Github 코드네임이 변경 되었습니다",
    }
  }), 200

@app.route("/setPresentation", methods=["POST"])
def setPresentation():
  if not request.is_json:
    return "Please request by JSON", 400
  
  presentation = request.json.get("presentation", None)
  
  try:
    cursor = db.cursor()
    cursor.execute("UPDATE profile SET presentation = %s WHERE id = 1", (presentation))
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  return jsonify({
    "status": {
      "success": True,
      "message": "자기소개 메시지가 변경 되었습니다",
    }
  }), 200

@app.route("/setProfilePhoto", methods=["POST"])
def setProfilePhoto():
  # check if the post request has the file part
  if "file" not in request.files:
    return jsonify({
      "status": {
        "success": False,
        "message": "폼데이터에 파일이 없습니다",
      }
    }), 200
  newFile = request.files["file"]
  if newFile.filename == "":
    return jsonify({
      "status": {
        "success": False,
        "message": "파일이 선택되지 않았습니다",
      }
    }), 200
  if newFile and isAllowedFile(newFile.filename, "image") == True:
    # Create profile directory if not exist
    if not os.path.isdir(os.path.join(app.root_path, "view", "data")):
      os.mkdir(os.path.join(app.root_path, "view", "data"))
    if not os.path.isdir(os.path.join(app.root_path, "view", "data", "profile")):
      os.mkdir(os.path.join(app.root_path, "view", "data", "profile"))
    else:
      # Delete previous image file
      previousFile = glob.glob(os.path.join(app.root_path, "view", "data", "profile", "profilePhoto.*"))
      for targetFile in previousFile:
        os.remove(os.path.join(app.root_path, "view", "data", "profile", targetFile))

    filename = "profilePhoto" + getExtension(newFile.filename)
    newFile.save(os.path.join(app.root_path, "view", "data", "profile", filename))
    url = "data/profile/" + filename
    
    try:
      cursor = db.cursor()
      cursor.execute("UPDATE profile SET photo = %s WHERE id = 1", (url))
      db.commit()
    except Exception as error:
      print(error)
      return jsonify({
        "status": {
          "success": False,
          "message": "데이터베이스에 오류가 발생했습니다",
        }
      }), 200
    finally:
      cursor.close()

    return jsonify({
      "status": {
        "success": True,
        "message": "프로필 사진이 변경 되었습니다",
      },
      "url": url
    }), 200

  return jsonify({
    "status": {
      "success": False,
      "message": "허용되지 않는 파일입니다",
    }
  }), 200

@app.route("/getActivity", methods=["GET"])
def getActivity():
  try:
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM activity")
    activityList = cursor.fetchall()
    json.dumps( [dict(ix) for ix in activityList] )
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  return jsonify({
    "status": {
      "success": True,
      "message": "활동이력 조회 성공",
    },
    "activityList": activityList
  }), 200

@app.route("/createActivity", methods=["POST"])
def createActivity():
  if not request.is_json:
    return "Please request by JSON", 400
  
  activity = request.json

  try:
    cursor = db.cursor()
    cursor.execute("INSERT INTO activity (content, timestamp) VALUE (%s, %s)", (activity["content"], activity["timestamp"]))
    db.commit()
    cursor.execute("SELECT * FROM activity WHERE content = %s AND timestamp = %s", (activity["content"], activity["timestamp"]))
    activity = cursor.fetchone()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()
  print(activity)
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

@app.route("/modifyActivity", methods=["POST"])
def modifyActivity():
  if not request.is_json:
    return "Please request by JSON", 400
  
  activity = request.json

  try:
    cursor = db.cursor()
    cursor.execute("UPDATE activity SET content = %s, timestamp = %s WHERE id = %s", (activity["content"], activity["timestamp"], activity["id"]))
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  return jsonify({
    "status": {
      "success": True,
      "message": "활동이력이 수정 되었습니다",
    },
    "activity": activity
  }), 200

@app.route("/deleteActivity", methods=["POST"])
def deleteActivity():
  if not request.is_json:
    return "Please request by JSON", 400
  
  activityID = request.json.get("id", None)

  try:
    cursor = db.cursor()
    cursor.execute("DELETE FROM activity WHERE id = %s", (activityID))
    db.commit()
  except Exception as error:
    print(error)
    return jsonify({
      "status": {
        "success": False,
        "message": "데이터베이스에 오류가 발생했습니다",
      }
    }), 200
  finally:
    cursor.close()

  return jsonify({
    "status": {
      "success": True,
      "message": "활동이력이 삭제 되었습니다",
    }
  }), 200

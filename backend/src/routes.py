from flask import render_template, request, redirect, jsonify, url_for, session
from . import app

# DB
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app.secret_key = 'asdfsadfasf'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'page'
app.config['MYSQL_PASSWORD'] = 'page'
app.config['MYSQL_DB'] = 'auth'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

# cors
from flask_cors import CORS, cross_origin
CORS(app, resources={r'*': {'origins': 'http://localhost:8080'}})

# route
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  if not request.is_json:
    return "Please request by JSON", 400
  
  username = request.json.get('username', None)
  password = request.json.get('password', None)
  
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))

  account = cursor.fetchone()
  if account:
    session['loggedIn'] = True
    session['id'] = account['id']
    session['username'] = account['username']
    session['permission'] = account['permission']
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

@app.route('/checkSession', methods=['POST'])
def checkSession():
  if not request.is_json:
    return "Please request by JSON", 400

  if session:
    if session['loggedIn'] == True:
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

@app.route('/logout', methods=['POST'])
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

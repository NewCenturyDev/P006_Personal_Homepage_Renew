from . import app
from flask_cors import CORS, cross_origin
# 개발 서버로 Frontend 구동시 Backend 테스트가 가능하도록 Cross-Origin 설정
CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})

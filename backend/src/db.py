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
DICT_CURSOR = pymysql.cursors.DictCursor

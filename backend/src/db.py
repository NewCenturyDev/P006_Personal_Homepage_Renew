# DB
import pymysql
config = {
  'host': "localhost",
  'port': 3306,
  'user': "page",
  'passwd': "page",
  'db': "page",
  'charset': "utf8"
}
def get_DB_connection():
  return pymysql.connect(**config)
DICT_CURSOR = pymysql.cursors.DictCursor

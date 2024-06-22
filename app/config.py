import os
import pymysql.cursors

SECRET_KEY = os.urandom(24)
# class Config:
#    SECRET_KEY = os.environ.get('SECRET_KEY') or '1718462882065'
#    MYSQL_HOST = 'localhost'
#    MYSQL_USER = 'root'
#    MYSQL_PASSWORD = '123456'
#    MYSQL_DB = 'student_system'
#    MYSQL_CURSORCLASS = 'DictCursor'  # 使得查询返回字典形式

# # 数据库连接配置
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "student_system",
    "charset": "utf8",
    "cursorclass": pymysql.cursors.DictCursor,
}

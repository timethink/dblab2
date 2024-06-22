import pymysql
from config import DB_CONFIG
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def all_classes():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM class'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def all_courses():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM course'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def all_majors():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM major'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def all_students():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def all_student_courses():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student_course'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def class_info(class_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM class WHERE id=%s'
    cursor.execute(sql, (class_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def course_info(course_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM course WHERE id=%s'
    cursor.execute(sql, (course_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def major_info(major_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM major WHERE id=%s'
    cursor.execute(sql, (major_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def student_info(student_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student WHERE id=%s'
    cursor.execute(sql, (student_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def student_course_info(student_id, course_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student_course WHERE student_id=%s AND course_id=%s'
    cursor.execute(sql, (student_id, course_id))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def students_in_class(class_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student WHERE class_id=%s'
    cursor.execute(sql, (class_id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def students_in_major(major_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = 'SELECT * FROM student WHERE major_id=%s'
    cursor.execute(sql, (major_id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def courses_of_student(student_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = '''
    SELECT course.id, course.name, course.credit, student_course.study_time, student_course.score
    FROM student_course
    JOIN course ON student_course.course_id = course.id
    WHERE student_course.student_id=%s
    '''
    cursor.execute(sql, (student_id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def top_students():
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    next_month = (datetime.now() + relativedelta(months=1)).replace(day=1).strftime('%Y-%m-%d')
    sql = '''
    SELECT student.id, student.name, AVG(student_course.score) AS avg_score
    FROM student_course
    JOIN student ON student_course.student_id = student.id
    WHERE student_course.study_time BETWEEN %s AND %s
    GROUP BY student.id
    ORDER BY avg_score DESC
    LIMIT 3
    '''
    cursor.execute(sql, (date, next_month))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def student_credit_history(student_id):
    db = pymysql.connect(**DB_CONFIG)
    cursor = db.cursor()
    sql = '''
    SELECT student_course.study_time, student_course.score, course.name, course.credit
    FROM student_course
    JOIN course ON student_course.course_id = course.id
    WHERE student_course.student_id=%s
    ORDER BY student_course.study_time DESC
    '''
    cursor.execute(sql, (student_id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

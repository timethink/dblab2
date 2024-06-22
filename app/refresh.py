import pymysql
from datetime import datetime, timedelta
from config import DB_CONFIG

def update_class_teacher(class_id, new_teacher):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "UPDATE class SET class_teacher=%s WHERE id=%s"
        cursor.execute(sql, (new_teacher, class_id))
        connection.commit()
    connection.close()

def update_course_name(course_id, new_name):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "UPDATE course SET name=%s WHERE id=%s"
        cursor.execute(sql, (new_name, course_id))
        connection.commit()
    connection.close()


def upload_img(fid, file):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = 'UPDATE Course SET path=%s WHERE fid=%s'
        cursor.execute(sql, (file, fid))
        connection.commit()
    connection.close()


def update_major_name(major_id, new_name):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "UPDATE major SET name=%s WHERE id=%s"
        cursor.execute(sql, (new_name, major_id))
        connection.commit()
    connection.close()

def update_student_course(student_id, course_id, study_time, score):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "UPDATE student_course SET study_time=%s, score=%s WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (study_time, score, student_id, course_id))
        connection.commit()
    connection.close()


def delete_student(student_id):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "DELETE FROM student WHERE id=%s"
        cursor.execute(sql, (student_id,))
        connection.commit()
    connection.close()

def delete_course(course_id):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "DELETE FROM course WHERE id=%s"
        cursor.execute(sql, (course_id,))
        connection.commit()
    connection.close()

def delete_student_course(student_id, course_id):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "DELETE FROM student_course WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        connection.commit()
    connection.close()

def insert_class(class_id, number, class_teacher):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "INSERT INTO class (id, number, class_teacher) VALUES (%s, %s, %s)"
        cursor.execute(sql, (class_id, number, class_teacher))
        connection.commit()
    connection.close()

def insert_course(course_id, credit, name):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "INSERT INTO course (id, credit, name) VALUES (%s, %s, %s)"
        cursor.execute(sql, (course_id, credit, name))
        connection.commit()
    connection.close()

def insert_major(major_id, name, number):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "INSERT INTO major (id, name, number) VALUES (%s, %s, %s)"
        cursor.execute(sql, (major_id, name, number))
        connection.commit()
    connection.close()

def insert_student(student_id, name, sex, birth_date, grade, class_id, major_id):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "INSERT INTO student (id, name, sex, birth_date, grade, class_id, major_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (student_id, name, sex, birth_date, grade, class_id, major_id))
        connection.commit()
    connection.close()

def insert_student_course(student_id, course_id, study_time, score):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        sql = "INSERT INTO student_course (student_id, course_id, study_time, score) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (student_id, course_id, study_time, score))
        connection.commit()
    connection.close()

def change_major(student_id, major_id):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        #调用过程CREATE PROCEDURE change_major(
        #IN student_id CHAR(10),
        #IN new_major_id VARCHAR(20),
        #OUT state INT -- 0: 成功, 1: 学生不存在, 2: 专业不存在, 3: 专业人数已满
        #)
        sql = "CALL change_major(%s, %s, @state)"
        cursor.execute(sql, (student_id, major_id))
        cursor.execute("SELECT @state")
        state = cursor.fetchone()['@state']
        connection.commit()
    connection.close()
    return state

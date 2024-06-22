from flask import Flask, render_template, request, redirect, url_for
import query
import refresh
from img import *
from config import DB_CONFIG
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = '2024db'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 允许上传的文件类型
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为16MB


@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # 返回新上传图片的文件名
        return filename
    return 'Error uploading image'


@app.route('/classes', methods=['GET', 'POST'])
def classes():
    classes = query.all_classes()
    return render_template('classes.html', classes=classes)
def add_class():
    if request.method == 'POST':
        class_id = request.form['id']
        number = request.form['number']
        class_teacher = request.form['class_teacher']
        refresh.insert_class(class_id, number, class_teacher)
        return redirect(url_for('classes'))
    #return render_template('add_class.html')
def delete_class():
    if request.method == 'POST':
        class_id = request.form['id']
        refresh.delete_class(class_id)
        return redirect(url_for('classes'))


@app.route('/courses')
def courses():
    courses = query.all_courses()
    return render_template('courses.html', courses=courses)

@app.route('/majors')
def majors():
    majors = query.all_majors()
    return render_template('majors.html', majors=majors)

@app.route('/students')
def students():
    students = query.all_students()
    return render_template('students.html', students=students)

@app.route('/filter_student', methods=['GET', 'POST'])
def filter_student():
    if request.method == 'POST':
        student_id = request.form['id']
        student = query.student_info(student_id)
        return render_template('filter_student.html', student=student)
    return render_template('filter_student.html')

@app.route('/student_courses')
def student_courses():
    student_courses = query.all_student_courses()
    return render_template('student_courses.html', student_courses=student_courses)

@app.route('/add_class', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        message = '请添加班级信息'
        class_id = request.form['id']
        number = request.form['number']
        class_teacher = request.form['class_teacher']
        refresh.insert_class(class_id, number, class_teacher)
    return render_template('add_class.html')

@app.route('/update_class_teacher', methods=['GET', 'POST'])
def update_class_teacher():
    if request.method == 'POST':
        message = '请更新班级教师'
        class_id = request.form['id']
        class_teacher = request.form['class_teacher']
        refresh.update_class_teacher(class_id, class_teacher)
    return render_template('update_class_teacher.html')

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_id = request.form['id']
        credit = request.form['credit']
        name = request.form['name']
        refresh.insert_course(course_id, credit, name)
        return redirect(url_for('courses'))
    return render_template('add_course.html')



@app.route('/delete_course', methods=['GET', 'POST'])
def delete_course():
    if request.method == 'POST':
        course_id = request.form['id']
        refresh.delete_course(course_id)
        return redirect(url_for('courses'))
    return render_template('delete_course.html')

@app.route('/add_major', methods=['GET', 'POST'])
def add_major():
    if request.method == 'POST':
        major_id = request.form['id']
        name = request.form['name']
        number = request.form['number']
        refresh.insert_major(major_id, name, number)
        return redirect(url_for('majors'))
    return render_template('add_major.html')

@app.route('/update_major_name', methods=['GET', 'POST'])
def update_major_name():
    if request.method == 'POST':
        major_id = request.form['id']
        new_name = request.form['major_name']
        refresh.update_major_name(major_id, new_name)
        return redirect(url_for('majors'))
    return render_template('update_major_name.html')

@app.route('/change_major_name', methods=['GET', 'POST'])
def change_major():
    if request.method == 'POST':
        student_id = request.form['student_id']
        major_id = request.form['major_id']
        refresh.change_major(student_id, major_id)
        #输出change_major得到的结果
        return redirect(url_for('majors'))
    return render_template('change_major.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['id']
        name = request.form['name']
        sex = request.form['sex']
        birth_date = request.form['birth_date']
        grade = request.form['grade']
        class_id = request.form['class_id']
        major_id = request.form['major_id']
        refresh.insert_student(student_id, name, sex, birth_date, grade, class_id, major_id)
        return redirect(url_for('students'))
    return render_template('add_student.html')

@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        student_id = request.form['id']
        refresh.delete_student(student_id)
        return redirect(url_for('students'))
    return render_template('delete_student.html')



@app.route('/update_course_name', methods=['GET', 'POST'])
def update_course_name():
    if request.method == 'POST':
        course_id = request.form['id']
        new_name = request.form['new_name']
        refresh.update_course_name(course_id, new_name)
        return redirect(url_for('courses'))

@app.route('/add_student_course', methods=['GET', 'POST'])
def add_student_course():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        study_time = request.form['study_time']
        score = request.form['score']
        refresh.insert_student_course(student_id, course_id, study_time, score)
        return redirect(url_for('student_courses'))
    return render_template('add_student_course.html')

@app.route('/delete_student_course', methods=['GET', 'POST'])
def delete_student_course():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        refresh.delete_student_course(student_id, course_id)
        return redirect(url_for('student_courses'))
    return render_template('delete_student_course.html')


@app.route('/update_student_course', methods=['GET', 'POST'])
def update_student_course():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        study_time = request.form['study_time']
        score = request.form['score']
        refresh.update_student_course(student_id, course_id, study_time, score)
        return redirect(url_for('student_courses'))
    return render_template('update_student_course.html')



if __name__ == '__main__':
    app.run(debug=True)

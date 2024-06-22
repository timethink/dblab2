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
-- 插入 class 表的数据




INSERT INTO class (id, number, class_teacher) VALUES
('C01', 30, 'Mr. Zhang'),
('C02', 28, 'Ms. Li');

-- 插入 major 表的数据
INSERT INTO major (id, name, number) VALUES
('M01', 'Computer Science', 100),
('M02', 'Mathematics', 80);

-- 插入 student 表的数据
INSERT INTO student (id, name, sex, birth_date, grade, class_id, major_id) VALUES
('S01', 'Alice', 'F', '2000-01-01', 'Freshman', 'C01', 'M01'),
('S02', 'Bob', 'M', '1999-12-12', 'Sophomore', 'C02', 'M02'),
('S03', 'Charlie', 'M', '2001-03-15', 'Junior', 'C01', 'M01'),
('S04', 'Diana', 'F', '2002-05-21', 'Freshman', 'C02', 'M02'),
('S05', 'Edward', 'M', '1998-07-10', 'Senior', 'C01', 'M02'),
('S06', 'Fiona', 'F', '2000-11-30', 'Sophomore', 'C02', 'M01'),
('S07', 'George', 'M', '2001-08-25', 'Junior', 'C01', 'M01'),
('S08', 'Hannah', 'F', '1999-09-15', 'Senior', 'C02', 'M02');

-- 插入 course 表的数据
INSERT INTO course (id, credit, name) VALUES
('C001', 3, 'Database Systems'),
('C002', 4, 'Algorithms');

-- 插入 student_course 表的数据
INSERT INTO student_course (student_id, course_id, study_time, score) VALUES
('S01', 'C001', 1, 85),
('S02', 'C002', 2, 90);

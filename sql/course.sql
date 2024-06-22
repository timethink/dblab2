use student_system;

DROP TRIGGER IF EXISTS before_insert_course;
-- 创建触发器以确保插入 course 表时 course_ID 唯一
DELIMITER //
create trigger before_insert_course
before insert on course
for each row
begin
    -- 检查 course 是否存在
    if exists(select * from course where id = new.id) then
        -- 检查 course 信息是否一致
        if not exists(select * from course 
                      where id = new.id and credit = new.credit  and name = new.name) then
            signal sqlstate '45000' set message_text = 'course 信息不一致';
        end if;
        -- 阻止插入
        signal sqlstate '45000' set message_text = 'course 已存在';
    end if;
end//
DELIMITER ;

DROP TRIGGER IF EXISTS before_insert_student_course;
-- 创建触发器以确保插入 student_course 表时的数据一致性
DELIMITER //
create trigger before_insert_student_course
before insert on student_course
for each row
begin
    -- 检查 student 是否存在
    if not exists(select * from student where id = new.student_id) then
        signal sqlstate '45001' set message_text = 'student 不存在';
    end if;
    -- 检查 course 是否存在
    if not exists(select * from course where id = new.course_id) then
        signal sqlstate '45003' set message_text = 'course 不存在';
    end if;
    -- 检查 study_time 是否合法，范围为 1-8
    if new.study_time < 1 or new.study_time > 8 then
        signal sqlstate '45005' set message_text = 'study_time 不合法';
    end if;
    -- 检查 score 是否合法
    if new.score < 0 or new.score > 100 then
        signal sqlstate '45005' set message_text = 'score 不合法';
    end if;
    -- 检查学生是否已经选过该课程
    if exists(select * from student_course where student_id = new.student_id and course_id = new.course_id) then
        signal sqlstate '45006' set message_text = '学生已经选过该课程';
    end if;
end//
DELIMITER ;

DROP TRIGGER IF EXISTS before_delete_course;
-- 创建触发器以确保删除 course 时的级联删除
DELIMITER //
create trigger before_delete_course
before delete on course
for each row
begin
    -- 删除相关的 student_course 记录
    delete from student_course where course_id = old.id;
end//
DELIMITER ;




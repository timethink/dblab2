use student_system;

DROP TRIGGER IF EXISTS before_insert_student;
DELIMITER //
-- 创建触发器以确保插入 student 表时 student_ID 唯一,并且 class_id 和 major_id 存在,且sex为M或F,grade为Freshman,Sophomore,Junior,Senior
create trigger before_insert_student
before insert on student
for each row
begin
    -- 检查 student 是否存在
    if exists(select * from student where id = new.id) then
        signal sqlstate '45000' set message_text = 'student_ID 已存在';
    end if;
    -- 检查 class_id 是否存在
    if not exists(select * from class where id = new.class_id) then
        signal sqlstate '45001' set message_text = 'class_id 不存在';
    end if;
    -- 检查 major_id 是否存在
    if not exists(select * from major where id = new.major_id) then
        signal sqlstate '45002' set message_text = 'major_id 不存在';
    end if;
    -- 检查sex是否为M或F
    if new.sex not in ('M','F') then
        signal sqlstate '45003' set message_text = 'sex 不合法';
    end if;
    -- 检查grade是否为Freshman,Sophomore,Junior,Senior
    if new.grade not in ('Freshman','Sophomore','Junior','Senior') then
        signal sqlstate '45003' set message_text = 'grade 不合法';
    end if;
end//
DELIMITER ;

DROP TRIGGER IF EXISTS before_delete_student;
-- 创建触发器以确保删除 student 时的级联删除
DELIMITER //
create trigger before_delete_student
before delete on student
for each row
begin
    -- 删除相关的 student_course 记录
    delete from student_course where student_id = old.id;
end//
DELIMITER ;
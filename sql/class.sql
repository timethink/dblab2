use student_system;

DROP TRIGGER IF EXISTS before_insert_class;
-- 创建触发器以确保插入 class 表时 class_ID 唯一
DELIMITER / /

create trigger before_insert_class
before insert on class
for each row
begin
    -- 检查 class 是否存在
    if exists(select * from class where id = new.id) then
        -- 检查 class 信息是否一致
        if not exists(select * from class 
                      where id = new.id and number = new.number and class_teacher = new.class_teacher) then
            signal sqlstate '45000' set message_text = 'class 信息不一致';
        end if;
        -- 阻止插入
        signal sqlstate '45000' set message_text = 'class 已存在';
    end if;
end//

DELIMITER;
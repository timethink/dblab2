USE student_system;

DROP TRIGGER IF EXISTS before_insert_major;
-- 创建触发器以确保插入 major 表时 major_ID 唯一
DELIMITER //
CREATE TRIGGER before_insert_major
BEFORE INSERT ON major
FOR EACH ROW
BEGIN
    -- 检查 major 是否存在
    IF EXISTS(SELECT * FROM major WHERE id = NEW.id) THEN
        -- 检查 major 信息是否一致
        IF NOT EXISTS(SELECT * FROM major 
                      WHERE id = NEW.id AND name = NEW.name AND number = NEW.number) THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'major 信息不一致';
        END IF;
        -- 阻止插入
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'major 已存在';
    END IF;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS change_major;
-- 创建存储过程以更改学生的专业,需要用到事务
DELIMITER //
CREATE PROCEDURE change_major(
    IN student_id CHAR(10),
    IN new_major_id VARCHAR(20),
    OUT state INT -- 0: 成功, 1: 学生不存在, 2: 专业不存在, 3: 专业人数已满
)
BEGIN
    DECLARE old_major_id VARCHAR(20);
    DECLARE old_major_name VARCHAR(20);
    DECLARE new_major_name VARCHAR(20);
    DECLARE old_major_number INT;
    DECLARE new_major_number INT;

    DECLARE exit handler for sqlexception 
    BEGIN 
        ROLLBACK; 
        SET state = 4; -- 任意错误时返回状态 4
    END;

    change_major: BEGIN
        -- 检查 student 是否存在
        IF NOT EXISTS(SELECT * FROM student WHERE id = student_id) THEN
            SET state = 1;
            LEAVE change_major;
        END IF;

        -- 检查 new_major 是否存在
        IF NOT EXISTS(SELECT * FROM major WHERE id = new_major_id) THEN
            SET state = 2;
            LEAVE change_major;
        END IF;

        -- 获取 student 的原专业
        SELECT major_id INTO old_major_id FROM student WHERE id = student_id;
        SELECT name INTO old_major_name FROM major WHERE id = old_major_id;
        SELECT name INTO new_major_name FROM major WHERE id = new_major_id;
        SELECT number INTO old_major_number FROM major WHERE id = old_major_id;
        SELECT number INTO new_major_number FROM major WHERE id = new_major_id;

        -- 检查新专业人数是否已满,即新专业人数是否大于等于专业人数上限10
        IF new_major_number >= 100 THEN
            SET state = 3;
            LEAVE change_major;
        END IF;

        -- 开始事务
        START TRANSACTION;
        -- 更新 student 的专业
        UPDATE student SET major_id = new_major_id WHERE id = student_id;
        -- 更新新专业人数
        UPDATE major SET number = new_major_number + 1 WHERE id = new_major_id;
        -- 更新旧专业人数
        UPDATE major SET number = old_major_number - 1 WHERE id = old_major_id;
        -- 提交事务
        COMMIT;
        SET state = 0;
    END change_major;
END//
DELIMITER ;

/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2024/5/21 0:29:09                            */
/*==============================================================*/

drop database if exists student_system;
create database student_system;
use student_system;
drop table if exists student;
drop table if exists study_course;
drop table if exists class;
drop table if exists course;
drop table if exists major;



/*==============================================================*/
/* Table: class                                                 */
/*==============================================================*/
create table class
(
   id             varchar(20) not null ,
   number         int not null ,
   class_teacher        varchar(20) not null ,
   CONSTRAINT PK_CLASS PRIMARY KEY (id)
);

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   id                 varchar(50) not null ,
   credit               int not null ,
   name          varchar(50) not null ,
   CONSTRAINT PK_COURSE PRIMARY KEY (id)
);



/*==============================================================*/
/* Table: major                                                 */
/*==============================================================*/
create table major
(
   id          varchar(20) not null ,
   name          varchar(20) not null ,
   number         int not null ,
   CONSTRAINT PK_MAJOR PRIMARY KEY (id)
);


/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   id               char(10) not null ,
   name             varchar(20) not null ,
   sex              varchar(5) not null ,
   birth_date           date not null ,
   grade                varchar(10) not null ,
   class_id             varchar(20) not null ,
   major_id             varchar(20) not null ,
   CONSTRAINT PK_STUDENT PRIMARY KEY (id),
   -- 外键有班级和专业
   constraint FK_STUDENT_CLASS_STUDENT foreign key (class_id) references class (id),
   constraint FK_STUDENT_MAJOR_STUDENT foreign key (major_id) references major (id)
);

/*==============================================================*/
/* Table: study_course                                          */
/*==============================================================*/
create table student_course
(
   student_id          char(10) not null ,
   course_id           varchar(50) not null ,
   study_time           int not null, #1表示大一上学期，2表示大一下学期，3表示大二上学期，4表示大二下学期，5表示大三上学期，6表示大三下学期，7表示大四上学期，8表示大四下学期
   score                int ,
   CONSTRAINT PK_STUDENT_COURSE PRIMARY KEY (student_id, course_id),
   constraint FK_STUDENT_CO_STUDENT_COURSE_STUDENT foreign key (student_id) references student (id) ,
   constraint FK_STUDENT_CO_STUDENT_COURSE_COURSE foreign key (course_id) references course (id)
);

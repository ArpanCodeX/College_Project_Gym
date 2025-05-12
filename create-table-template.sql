CREATE TABLE users(  
    id int NOT NULL  AUTO_INCREMENT COMMENT 'Primary Key',
    name varchar(255) NOT NULL COMMENT 'User Name',
    password varchar(255) NOT NULL COMMENT 'User Password',
    create_time DATETIME COMMENT 'Create Time',
    PRIMARY key (id)
) COMMENT 'done';
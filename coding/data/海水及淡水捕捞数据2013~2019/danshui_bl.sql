-- Active: 1670156131320@@127.0.0.1@3306@sem
use sem;
CREATE TABLE danshui_bl(`city` VARCHAR(40) NOT NULL,
                    `year` INT,
                    `kind` VARCHAR(100) NOT NULL,
                    `num` INT
                    );
select * from danshui_bl LIMIT 0, 2000
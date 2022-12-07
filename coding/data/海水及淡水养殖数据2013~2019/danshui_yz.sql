use yv;
CREATE TABLE danshui_yz(`city` VARCHAR(40) NOT NULL,
                    `year` INT,
                    `kind` VARCHAR(100) NOT NULL,
                    `num` INT
                    );
select * from danshui_yz LIMIT 0, 2000
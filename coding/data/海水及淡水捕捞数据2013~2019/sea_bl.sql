
use yv;
CREATE TABLE sea_bl(`city` VARCHAR(40) NOT NULL,
                    `year` INT,
                    `kind` VARCHAR(100) NOT NULL,
                    `num` INT
                    );
select * from sea_bl LIMIT 0, 2000
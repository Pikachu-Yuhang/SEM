
use yv;
CREATE TABLE yycz_nj(`city` VARCHAR(40) NOT NULL,
                    `year` INT,
                    `kind` VARCHAR(100) NOT NULL,
                    `num` INT
                    );
select * from yycz_nj LIMIT 0, 2000
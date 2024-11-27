-- define a table
CREATE TABLE datachilly_student (
    name TEXT,
    age INT
);

-- manipulate data in the table
INSERT INTO datachilly_student (name, age) VALUES
('Nguyen Van A', 22),
('Tran Van B', 25);

-- query data from the table
SELECT * FROM datachilly_student;
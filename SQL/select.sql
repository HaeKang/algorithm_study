-- 프로그래머스 SELECT

SELECT * from animal_ins order by animal_id

SELECT name, datetime from animal_ins order by animal_id desc;

SELECT animal_id, name from animal_ins where intake_condition = "Sick";

SELECT animal_id, name from animal_ins where intake_condition != "Aged" order by animal_id;

SELECT animal_id, name from animal_ins order by animal_id;

SELECT animal_id, name, datetime from animal_ins order by name, datetime desc;

SELECT name from animal_ins order by datetime limit 1
SELECT name from animal_ins where datetime = (select min(datetime) from animal_ins);

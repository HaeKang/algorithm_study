SELECT animal_type, count(animal_type) as count from animal_ins where animal_type = "Dog" or animal_type="Cat" group by animal_type order by animal_type asc;

SELECT name, count(name) as count from animal_ins group by name having count(name) >=2 order by name;

select HOUR(datetime) as HOUR, count(animal_id) as count 
from animal_outs 
group by HOUR(datetime)
having HOUR >= 9 and HOUR <=19
order by HOUR;




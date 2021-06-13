select outs.animal_id, outs.name 
from animal_outs outs left outer join animal_ins ins
on outs.ANIMAL_ID = ins.ANIMAL_ID
where ins.animal_id is null
order by outs.animal_id;


SELECT ins.animal_id, ins.name
from animal_ins ins left join animal_outs outs
on ins.animal_id = outs.animal_id
where ins.datetime > outs.datetime
order by ins.datetime;


SELECT ins.name, ins.datetime
from animal_ins ins left join animal_outs outs
on ins.animal_id = outs.animal_id
where outs.animal_id is null
order by ins.datetime 
limit 3


SELECT outs.animal_id, outs.animal_type, outs.name
from animal_outs outs join animal_ins ins
on outs.animal_id = ins.animal_id
where (ins.SEX_UPON_INTAKE like 'Intact%') and 
(outs.SEX_UPON_OUTCOME like 'Spayed%' or outs.SEX_UPON_OUTCOME like 'Neutered%')
order by outs.animal_id;

select w.id, p.age, w.coins_needed, w.power
from wands as w
join wands_property as p
on w.code = p.code
where w.coins_needed = (select min(coins_needed)
                       from wands
                       join wands_property
                       on wands.code = wands_property.code
                       where wands_property.is_evil = 0 and wands_property.age = p.age and w.power = wands.power)
order by w.power desc, p.age desc

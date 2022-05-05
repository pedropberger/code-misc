/*A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

The STATION table is described as follows:

where LAT_N is the northern latitude and LONG_W is the western longitude.*/

select round(lat_n,4)
from (select row_number() over (order by lat_n) as row_id, lat_n from station) as t
where row_id = (select round(count(lat_n)/2,0) from station)

-- BANG: simpler soluction than from interwebs

SELECT * FROM dataset_1 ;

SELECT weather,temperature FROM dataset_1 ;

SELECT * FROM dataset_1 LIMIT 5;

SELECT DISTINCT passanger FROM dataset_1;


SELECT * FROM dataset_1 WHERE destination = 'Home';


SELECT * FROM dataset_1 ORDER BY coupon ;

SELECT destination as Destination FROM dataset_1;

SELECT  occupation FROM dataset_1 GROUP  BY occupation ;

SELECT weather ,AVG(temperature) as avg_temp FROM dataset_1 GROUP BY weather;


SELECT  weather, COUNT(temperature) as count_temp FROM  dataset_1 GROUP BY weather ;

SELECT  weather, COUNT(DISTINCT temperature) as count_distinct_temp FROM  dataset_1 GROUP BY weather ;


SELECT  weather, SUM(temperature) as sum_temp FROM  dataset_1 GROUP BY weather ;


SELECT  weather, MIN(temperature) as min_temp FROM  dataset_1 GROUP BY weather ;



SELECT  weather, MAX(temperature) as max_temp FROM  dataset_1 GROUP BY weather 


SELECT occupation , count(occupation ) as coun FROM dataset_1 GROUP BY occupation ;
HAVING occupation = 'Student'


SELECT DISTINCT destination  FROM (SELECT * FROM dataset_1 UNION SELECT * FROM table_to_union);

SELECT a.destination,a.time,b.part_of_day FROM dataset_1 a INNER JOIN table_to_join b ON
a.time=b.time;

SELECT destination ,passanger FROM (SELECT*FROM dataset_1 WHERE passanger = 'Alone');


SELECT destination ,passanger FROM  dataset_1 WHERE passanger = 'Alone';

SELECT * FROM dataset_1 WHERE weather LIKE 'Sun%';

SELECT DISTINCT temperature FROM dataset_1 WHERE temperature BETWEEN 29 AND 75;

SELECT occupation FROM dataset_1 WHERE occupation IN('Sales & Related','Management');








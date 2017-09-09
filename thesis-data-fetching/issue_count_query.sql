SELECT title AS title, count(*) AS count
FROM lucene_try
GROUP BY title
HAVING ( COUNT(title) > 1 )
ORDER BY count DESC;



SELECT title AS title, count(*) AS count
FROM thunderbird_try
GROUP BY title
HAVING ( COUNT(title) > 1 )
ORDER BY count DESC;



SELECT title AS title, count(*) AS count
FROM ubuntu_try
GROUP BY title
HAVING ( COUNT(title) > 1 )
ORDER BY count DESC;

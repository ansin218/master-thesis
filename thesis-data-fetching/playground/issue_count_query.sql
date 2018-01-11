-- Filter Lucene
SELECT title AS title, count(*) AS count
FROM lucene_try
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

SELECT title AS title, count(*) AS count
FROM lucene_try
WHERE id < 53960
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

-- Filter Ubuntu
SELECT title AS title, count(*) AS count
FROM ubuntu_try
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

SELECT title AS title, count(*) AS count
FROM ubuntu_try
WHERE id >= 14567
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

-- Filter Thunderbird
SELECT title AS title, count(*) AS count
FROM thunderbird_try
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

SELECT title AS title, count(*) AS count
FROM thunderbird_try
WHERE id >= 28237
GROUP BY title
HAVING ( COUNT(title) >= 1 )
ORDER BY count DESC;

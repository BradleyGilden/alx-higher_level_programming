-- using groups in SQL
SELECT COUNT(score) AS `number`
FROM second_table
GROUP BY score
ORDER BY `number` DESC;

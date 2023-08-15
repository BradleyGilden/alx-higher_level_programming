-- lists rows which have a valid name entry
SELECT score, name
	FROM second_table
	WHERE name IS NOT NULL
	ORDER BY DESC;

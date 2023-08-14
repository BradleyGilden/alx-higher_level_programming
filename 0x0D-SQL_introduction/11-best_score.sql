-- lists table rows ordered by score value descending
SELECT score, name
    FROM second_table
    WHERE score >= 10
    ORDER BY score DESC;

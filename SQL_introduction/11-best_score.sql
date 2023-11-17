-- Lists all records with a score equal or bigger than 10 from the second_table.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
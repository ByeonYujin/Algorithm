CREATE PROCEDURE marketReport()
BEGIN
    SELECT IFNULL(country, "Total:") as country, COUNT(*) AS competitors
    FROM foreignCompetitors
    GROUP BY country WITH ROLLUP;
END

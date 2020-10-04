SELECT DISTINCT subscriber FROM (
        SELECT * FROM half_year
        UNION
        SELECT * FROM full_year
    ) union_table
    WHERE union_table.newspaper LIKE '%Daily%'
    ORDER BY SUBSTRING_INDEX(subscriber, ' ', 1);

CREATE PROCEDURE nullIntern()
BEGIN
    SELECT COUNT(*) AS number_of_nulls
    FROM departments
    WHERE UPPER(TRIM(description)) IN ("NULL", "NIL", "-") OR description IS NULL;
END

CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT * FROM expressions
    WHERE (CASE
        WHEN operation = '+' THEN a + b = c
        WHEN operation = '-' THEN a - b = c
        WHEN operation = '*' THEN a * b = c
        ELSE a / b = c
        END
    )
    ORDER BY id;
END

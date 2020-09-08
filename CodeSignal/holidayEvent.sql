CREATE PROCEDURE holidayEvent()
BEGIN
    SET @num = 0;
    SELECT DISTINCT buyer_name AS winners
    FROM purchases
    WHERE
        (@num := @num + 1) % 4 = 0
    ORDER BY 1;
END

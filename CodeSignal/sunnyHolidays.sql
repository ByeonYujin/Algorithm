CREATE PROCEDURE sunnyHolidays()
BEGIN
    SELECT holiday_date AS ski_date 
    FROM holidays
    WHERE holiday_date in (SELECT sunny_date FROM weather)
    ORDER BY holiday_date ASC; 
END

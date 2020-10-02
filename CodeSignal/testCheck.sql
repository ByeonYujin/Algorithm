CREATE PROCEDURE testCheck()
    SELECT id, (CASE
        WHEN given_answer IS NULL THEN 'no answer'
        WHEN given_answer LIKE correct_answer THEN 'correct'
        ELSE 'incorrect'
        END
    )
    AS checks
    FROM answers
    ORDER BY id;

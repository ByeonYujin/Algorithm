CREATE PROCEDURE websiteHacking()
    SELECT id,login,name
    FROM users
    WHERE type='user' or type is not null
    ORDER BY id;

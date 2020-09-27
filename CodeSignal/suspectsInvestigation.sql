CREATE PROCEDURE suspectsInvestigation()
BEGIN
    SELECT id, name, surname FROM Suspect
    WHERE height <= 170 AND name LIKE 'B%' AND surname LIKE 'Gre%n' AND LENGTH(surname) = 5
    ORDER BY id;
END

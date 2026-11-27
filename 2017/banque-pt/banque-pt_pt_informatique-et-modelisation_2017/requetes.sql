-- I24
CREATE TABLE table_injection_95 AS
SELECT *
FROM table_injection
WHERE "Qualité" > 95;

-- I25
WITH admissibles AS (
    SELECT Pression, Rotation, "Durée_injection", "Qualité"
    FROM table_injection_95
    WHERE Pression BETWEEN 0.3 AND 0.4
      AND Rotation BETWEEN 1300 AND 1700
)
SELECT Pression, Rotation, "Durée_injection"
FROM admissibles
WHERE "Qualité" = (SELECT MAX("Qualité") FROM admissibles);

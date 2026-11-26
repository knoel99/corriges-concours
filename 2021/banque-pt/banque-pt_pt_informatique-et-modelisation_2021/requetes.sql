-- Q36
SELECT id
FROM PHOTOS
WHERE date = '20181111';

-- Q37
SELECT g.nom, g.prenom
FROM PHOTOGRAPHES AS g
WHERE EXISTS (
    SELECT 1 FROM PHOTOS AS p
    WHERE p.idp = g.id AND p.date = '20181111'
);

-- Q38
SELECT g.nom, g.prenom, p.heure
FROM PHOTOS AS p
JOIN PHOTOGRAPHES AS g ON g.id = p.idp
WHERE p.date = '20181111';

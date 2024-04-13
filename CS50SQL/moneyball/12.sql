WITH HitCTE AS (
    SELECT p.id AS player_id, p.first_name, p.last_name
    FROM players p
    JOIN performances pf ON p.id = pf.player_id
    JOIN salaries s ON p.id = s.player_id AND pf.year = s.year
    WHERE pf.year = 2001
    AND pf.H > 0
    ORDER BY s.salary / NULLIF(pf.H, 0) ASC
    LIMIT 10
),

RbiCTE AS (
    SELECT p.id AS player_id, p.first_name, p.last_name
    FROM players p
    JOIN performances pf ON p.id = pf.player_id
    JOIN salaries s ON p.id = s.player_id AND pf.year = s.year
    WHERE pf.year = 2001
    AND pf.RBI > 0
    ORDER BY s.salary / NULLIF(pf.RBI, 0) ASC
    LIMIT 10
)

SELECT h.first_name, h.last_name
FROM HitCTE h
JOIN RbiCTE r ON h.player_id = r.player_id
ORDER BY h.player_id;

SELECT "name", SUM("H") AS "total hits" FROM "teams" AS "t"
JOIN "performances" AS "p" ON "t"."id" = "p"."team_id"
WHERE "p"."year" = 2001
GROUP BY "t"."name"
ORDER BY SUM("p"."H") DESC
LIMIT 5;


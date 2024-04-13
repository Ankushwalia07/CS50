SELECT "first_name", "last_name", "salary" FROM "players" AS "p"
JOIN "salaries" AS "s" ON "p"."id" = "s"."player_id"
WHERE "s"."year" = 2001
ORDER BY "s"."salary" ASC,"p"."first_name" ASC, "p"."last_name" ASC LIMIT 50;

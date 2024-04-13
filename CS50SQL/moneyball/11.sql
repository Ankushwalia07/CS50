SELECT "p"."first_name", "p"."last_name", "s"."salary" / "pr"."H" AS "dollars per hit" FROM "players" AS "p"
JOIN "salaries" AS "s" ON "p"."id" = "s"."player_id"
JOIN "performances" AS "pr" ON "p"."id" = "pr"."player_id" AND "s"."year" = "pr"."year"
WHERE "pr"."H" > 0 AND "s"."year" = 2001
ORDER BY "dollars per hit" ASC LIMIT 10;

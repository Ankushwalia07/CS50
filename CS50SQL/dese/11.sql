SELECT "name", "per_pupil_expenditure", "graduated" FROM "schools" AS "s"
JOIN "graduation_rates" as "g" ON "s"."id" = "g"."school_id"
JOIN "expenditures" as "e" ON "s"."district_id" = "e"."district_id"
ORDER BY "e"."per_pupil_expenditure" DESC, "s"."name" ASC;

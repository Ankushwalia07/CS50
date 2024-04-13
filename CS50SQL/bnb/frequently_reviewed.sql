CREATE VIEW "frequently_reviewed" AS
SELECT
	"l"."id",
	"l"."property_type",
	"l"."host_name",
	COUNT("r"."id") AS "reviews"
FROM "listings" AS "l"
INNER JOIN "reviews" AS "r" ON "l"."id" = "r"."listing_id"
GROUP BY
	 "l"."id",
	"l"."property_type",
	"l"."host_name"
ORDER BY
	COUNT("r"."id") DESC,
	"l"."property_type" ASC,
	"l"."host_name" ASC
LIMIT
	100;

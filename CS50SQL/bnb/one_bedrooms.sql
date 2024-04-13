CREATE VIEW "one_bedrooms" AS
SELECT "id", "property_type", "host_name", "acommodates" FROM "listings"
WHERE "bedrooms" = 1;

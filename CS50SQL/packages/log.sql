
-- *** The Lost Letter ***


-- Finidng the post address.
SELECT "id", "address", "type" FROM "addresses" WHERE "id" = (
    SELECT "to_address_id" FROM "packages" WHERE "contents" = 'Congratulatory letter'
); -- id = 854


-- *** The Devious Delivery ***
-- Query to Find where did the devious parcel ended up
SELECT "address", "type" FROM "addresses" WHERE "id" = (
    SELECT "address_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "from_address_id" IS NULL
    ) AND "action" = 'Drop'
);



-- Query to find the contents of devious package
SELECT "contents" FROM "packages" WHERE "from_address_id" IS NULL;


-- *** The Forgotten Gift ***

-- Finding the contnets of the missing package.
SELECT "contents", "id" FROM "packages" WHERE "to_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place'
);

-- Fiding driver
SELECT "name" FROM "drivers" WHERE "id" =(
    SELECT "driver_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "to_address_id" = (
            SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place'
        ) AND "contents" = 'Flowers'
    )
);


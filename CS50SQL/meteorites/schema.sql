.mode csv
.import meteorites.csv temp

CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "nametype" TEXT NOT NULL,
    "class" TEXT NOT NULL,
    "mass" NUMERIC,
    "discovery" TEXT NOT NULL CHECK ("discovery" IN ("Fell", "Found")),
    "year" NUMERIC,
    "lat" NUMERIC ,
    "long" NUMERIC,
    PRIMARY KEY ("id")
);

UPDATE "temp" SET "mass" = CASE WHEN "mass" = '' THEN NULL ELSE "mass" END;
UPDATE "temp" SET "year" = CASE WHEN "year" = '' THEN NULL ELSE "year" END;
UPDATE "temp" SET "lat" = CASE WHEN "lat" = '' THEN NULL ELSE "lat" END;
UPDATE "temp" SET "long" = CASE WHEN "long" = '' THEN NULL ELSE "long" END;

UPDATE "temp" SET "mass" = ROUND("mass", 2);
UPDATE "temp" SET "lat" = ROUND("lat", 2);
UPDATE "temp" SET "long" = ROUND("long", 2);


DELETE FROM "temp" WHERE "nametype" = 'Relict';


INSERT INTO "meteorites" ("id","name", "nametype", "class", "mass", "discovery", "year", "lat", "long")
SELECT "id" ,"name", "nametype", "class", "mass" , "discovery" , "year" , "lat" , "long"
FROM "temp"
ORDER BY "year" ASC, "name" ASC;

DROP TABLE "temp";

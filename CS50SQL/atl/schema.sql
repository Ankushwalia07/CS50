-- A table for passengers for first_name, last_name and age
CREATE TABLE "passengers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL ,
    "last_name" TEXT,
    "age", INTEGER NOT NULL,
    PRIMARY KEY("id")
);

-- Second table for Checkins
CREATE TABLE "check-in"(
    "passenger_id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight_to" TEXT NOT NULL,
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id")

);
-- Third table for Airlines
CREATE TABLE "airlines"(
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT NOT NULL

);

-- Fouth table for flights
CREATE TABLE "flights" (
    "passenger_id" INTEGER,
    "airline_id" INTEGER,
    "depart_code" TEXT NOT NULL UNIQUE,
    "heading_code" TEXT NOT NULL UNIQUE,
    "departure_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "arrival_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);

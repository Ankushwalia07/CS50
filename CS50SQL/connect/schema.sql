-- USERS TABLE
CREATE TABLE "users" (
    "username" TEXT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "password" TEXT,
    PRIMARY KEY("username")
);

-- Second Table
CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" NUMERIC NOT NULL,
    PRIMARY KEY("id")
);

-- Third table
CREATE TABLE "compaines" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- FOURTH Table
CREATE TABLE
	IF NOT EXISTS "connection_with_people" (
		"user_id_1" INTEGER,
		"user_id_2" INTEGER,
		PRIMARY KEY ("user_id_1", "user_id_2")
);

--

CREATE TABLE "connections_with_school"(
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "type" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")

);

CREATE TABLE "connections_with_company"(
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC NOT NULL,
    "title" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "compaines"("id")

);

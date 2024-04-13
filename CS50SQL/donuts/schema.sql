CREATE TABLE IF NOT EXISTS "ingredients" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT,
    "price_per_unit" DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS "donuts" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT,
    "ingredient_id" INTEGER,
    "is_gluten_free" BOOLEAN,
    "price_per_donut" DECIMAL(10, 2),
    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients" ("id")
);

CREATE TABLE IF NOT EXISTS "orders" (
    "id" INTEGER PRIMARY KEY,
    "order_number" VARCHAR(255),
    "customer_id" INTEGER,
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id")
);

CREATE TABLE IF NOT EXISTS "donuts_orders" (
    "id" INTEGER PRIMARY KEY,
    "order_id" INTEGER,
    "customer_id" INTEGER,
    FOREIGN KEY ("order_id") REFERENCES "orders" ("id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id")
);

CREATE TABLE IF NOT EXISTS "customers" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT
);

CREATE TABLE IF NOT EXISTS "customer_order_history" (
    "customer_id" INTEGER,
    "order_id" INTEGER,
    PRIMARY KEY ("customer_id", "order_id"),
    FOREIGN KEY ("customer_id") REFERENCES "customers" ("id"),
    FOREIGN KEY ("order_id") REFERENCES "orders" ("id")
);


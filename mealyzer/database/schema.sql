CREATE TABLE recipe (
    recipe_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    source TEXT,
    instructions TEXT,
    course TEXT,
    cuisine TEXT,
    cook_hours REAL
);

CREATE TABLE ingredient (
    ingredient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    default_unit TEXT NOT NULL,
    cost_per_unit REAL
);

CREATE TABLE recipe_ingredient (
    recipe_id TEXT NOT NULL,
    ingredient_id TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL,
    PRIMARY KEY (recipe_id, ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(id)
);

CREATE TABLE nutrition (
    nutrition_id INTEGER PRIMARY KEY,
    ingredient_id INTEGER,
    calories NUMERIC,
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id)
);
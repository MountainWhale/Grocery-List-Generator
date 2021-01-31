import sqlite3

table: str  = """
CREATE TABLE IF NOT EXISTS food (
	name TEXT UNIQUE NOT NULL,
	ingredients TEXT NOT NULL
);
"""

db = sqlite3.connect("recipes.sqlite")
cursor = db.cursor()

cursor.execute(table)
db.commit()

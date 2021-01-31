import sqlite3
import sys

name: str = sys.argv[1]
ingredients: str = " ".join(sys.argv[2::])

db = sqlite3.connect("recipes.sqlite")
cursor = db.cursor()

cursor.execute("INSERT INTO food (name, ingredients ) VALUES (?, ?)",
(name, ingredients))

db.commit()

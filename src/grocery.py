import sys
from typing import List
import sqlite3
import datetime

recipes: List[str] = sys.argv[1::]
db = sqlite3.connect("recipes.sqlite")
cursor = db.cursor()
ingredients: List[str] = []


for each in recipes:
	result = cursor.execute("SELECT ingredients FROM food WHERE name = ?",
				(each,)).fetchone()
	for x in result:
		temp: List[str] = x.split(",")
		for i in temp:
			if i.lower().strip() not in ingredients:
				ingredients.append(i.lower().strip())

date = datetime.datetime.now()
with open("grocery_list.md", "w+") as f:
	f.write(f"### Grocery List for {date.day}/{date.month}/{date.year}\n")
	for each in ingredients:
		f.write(f"- [] {each}\n")
f.close()

import uuid, sqlite3

recipes = [] # Λίστα όπου θα τοποθετηθούν αντικείμενα της κλάσης "Recipe"

# Test data for development and a class for the recipes
class Recipe:
	def __init__(self, name="", category="", difficulty="", time="", ingredients="", steps=""):
		'''
		Παράδειγμα συνταγής:
		spaghetti_meatballs = Recipe(name="Μακαρόνια με κιμά", category="Ζυμαρικά", difficulty="", time="", ingredients="", steps="")
		'''
		self.id = uuid.uuid4() # Μοναδικό πρωτεύον κλειδί για χρήση στην βάση δεδομένων
		self.name = name
		self.category = category
		self.difficulty = difficulty
		self.time = time
		self.ingredients = ingredients
		self.steps = steps

import time
vhmata = {
	"1": {"vhma": "Vrazoume to nero...", "xronos": time.time()},
	"2": {"vhma": "kimas...", "xronos": time.time()}
}

def save_recipe_to_db(recipe, db_name="recipes.db"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Make sure the table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id TEXT PRIMARY KEY,
            name TEXT,
            category TEXT,
            difficulty TEXT,
            time TEXT,
            ingredients TEXT,
            steps TEXT
        )
    ''')

    # Insert the recipe
    cursor.execute('''
        INSERT INTO recipes (id, name, category, difficulty, time, ingredients, steps)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (str(recipe.id), recipe.name, recipe.category, recipe.difficulty, recipe.time, recipe.ingredients, recipe.steps))

    # Commit and close
    conn.commit()
    conn.close()

def show_all_recipes(db_name="recipes.db"):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Select all recipes
    cursor.execute('SELECT id, name, category FROM recipes')
    recipes = cursor.fetchall()

    # Print each recipe
    if recipes:
        print("Recipes in database:")
        for recipe in recipes:
            print(f"ID: {recipe[0]}, Name: {recipe[1]}, Category: {recipe[2]}")
    else:
        print("No recipes found.")

    # Close the connection
    conn.close()


def filter_by_category(recipes, category):
	'''Η συνάρτηση αυτή δεν είναι ακόμη έτοιμη'''
	# ΠΡΕΠΕΙ ΝΑ ΞΑΝΑΓΡΑΦΤΕΙ ΜΕ SQLITE!!
	# ΘΑ ΚΑΛΟΥΜΕ ΤΗΝ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΓΙΑ ΝΑ ΒΡΕΙ ΤΙΣ ΣΥΝΓΑΓΕΣ
	# filtered = []
	# for i in recipes:
	# 	if i.category == category:
	# 		filtered.append(i)
	# return filtered
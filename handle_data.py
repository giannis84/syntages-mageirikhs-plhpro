import uuid, sqlite3, os
import definitions as defs


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

# import time
# vhmata = {
# 	"1": {"vhma": "Vrazoume to nero...", "xronos": time.time()},
# 	"2": {"vhma": "kimas...", "xronos": time.time()}
# }

def save_recipe_to_db(recipe):
    '''Αποθήκευση συνταγής'''
    # Σύνδεση στην βάση
    conn = sqlite3.connect(defs.DATABASE)
    cursor = conn.cursor()
    # Αρχικοποίηση TABLE εάν δεν υπάρχει
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
    # Εισαγωγή συνταγής
    cursor.execute('''
        INSERT INTO recipes (id, name, category, difficulty, time, ingredients, steps)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (str(recipe.id), recipe.name, recipe.category, recipe.difficulty, recipe.time, recipe.ingredients, recipe.steps))
    conn.commit()
    conn.close()

def show_all_recipes():
    db_name = defs.DATABASE
    '''Εκτύπωση όλων των συνταγών (για debugging)'''
    if not os.path.exists(db_name):
        print(f"Database file '{db_name}' does not exist.")
        return
    # Σύνδεση στην βάση
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, difficulty FROM recipes') # SELECT όλων των συνταγών
    recipes = cursor.fetchall()
    if recipes:
        print("Recipes in database:")
        for recipe in recipes:
            # print(f"ID: {recipe[0]}, Name: {recipe[1]}, Category: {recipe[2]}, Difficulty: {recipe}")
            print(recipe)
    else:
        print("No recipes found.")
    conn.close()


def filter_by_category(recipes, category):
	'''Η συνάρτηση αυτή δεν είναι ακόμη έτοιμη'''
	# ΠΡΕΠΕΙ ΝΑ ΞΑΝΑΓΡΑΦΤΕΙ ΜΕ SQLITE!!
	# ΘΑ ΚΑΛΟΥΜΕ ΤΗΝ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΓΙΑ ΝΑ ΒΡΕΙ ΤΙΣ ΣΥΝΓΑΓΕΣ
import uuid, sqlite3, os
import definitions as defs

# Κλάση Recipe - ορισμός συνταγής
class Recipe:
	def __init__(self, id="", name="", category="", difficulty="", time="", ingredients="", steps=""):
		'''
		Παράδειγμα συνταγής:
		spaghetti_meatballs = Recipe(name="Μακαρόνια με κιμά", category="Ζυμαρικά", difficulty="", time="", ingredients="", steps="")
		'''
		self.id = get_id(id) # Μοναδικό πρωτεύον κλειδί για χρήση στην βάση δεδομένων
		self.name = name
		self.category = category
		self.difficulty = difficulty
		self.time = time
		self.ingredients = ingredients
		self.steps = steps
          
def get_id(id):
     if id == "":
        id = uuid.uuid4()
     return id


# Κώδικας Βάσης Δεδομένων

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

def search_recipe_by_name(recipe_name):
    '''Η συνάρτηση αυτή δεν είναι ακόμη έτοιμη'''
    db_name = defs.DATABASE
    if not os.path.exists(db_name):
        return [Recipe()]  # Empty recipe if DB doesn't exist

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = '''
        SELECT id, name, category, difficulty, time, ingredients, steps
        FROM recipes
        WHERE name LIKE ?
    '''
    search_term = f'%{recipe_name}%'
    cursor.execute(query, (search_term,))
    results = cursor.fetchall()
    print(results)
    conn.close()

    if results:
        return [
            Recipe(
                id=r[0],
                name=r[1],
                category=r[2],
                difficulty=r[3],
                time=r[4],
                ingredients=r[5],
                steps=r[6]
            )
            for r in results
        ]
    else:
        return [Recipe()]  # Return list with one empty recipe
    

def delete_recipe_by_id(id):
    conn = sqlite3.connect(defs.DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (id,))
    conn.commit()
    conn.close()



# Debugging functions

def show_all_recipes():
    '''Συνάρτηση για debugging, δείχνει όλες τις συνταγές που έχουμε αποθηκεύσει'''
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
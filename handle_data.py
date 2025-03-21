import uuid

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


def filter_by_category(recipes, category):
	'''Η συνάρτηση αυτή δεν είναι ακόμη έτοιμη'''
	filtered = []
	for i in recipes:
		if i.category == category:
			filtered.append(i)
	return filtered
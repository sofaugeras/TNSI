class File:

	def __init__(self):
		self.valeurs = []
  
	def estFileVide(self):
		return self.valeurs == []
	
	def enfile(self, valeur):
		self.valeurs.append(valeur)

	def defile(self):
		if self.valeurs:
			return self.valeurs.pop(0)
	@property
	def longueur(self):
		return len(self.valeurs)

	def __str__(self):
		ch = "\nEtat de la file:\n"
		for x in self.valeurs:
			ch +=  str(x) + " "
		return ch
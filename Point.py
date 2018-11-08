class Point :
	""" Classe modélisant un point, fondement du cryptage elliptique
	On se concentres sur les coordonnées cartésiennes, qui seront des nombres premiers de grandes tailles
	Cette classe instanciera des points
	Fera l'addition de deux points 
	La distance entre ces deux points 

	"""
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __repr__(self):
		return "({} , {})".format(self.x,self.y)

	def add( self, a, b):
		return Point(a.x+b.x,a.y+b.y)

		
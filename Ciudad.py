import grafo
import math
import numpy as np

class Ciudad:
	def __init__(self):
		self.mapa = Grafo()
		self.coord_angulares = {}
		self.coord_metros = {}

	def calcular_distancia(self, esquina1, esquina2):
		coord_metros_1 = self.coord_metros[esquina1]
		coord_metros_2 = self.coord_metros[esquina2]
		dist = coord_metros_2 - coord_metros_1
		return math.hypot(dist[0], dist[1])

	def agregar_esquina(self, esquina, x, y, lat, lon):
		self.mapa.agregar_vertice(esquina)
		self.coord_metros[esquina] = np.array([x,y])
		self.coord_angulares[esquina] = np.array([lat,lon])

<<<<<<< .mine
	def agregar_calle(self, idc, esquina1, esquina2):
		dist  =  calcular_distancia(esquina1, esquina2)
		self.mapa.agregar_arista(esquina1, esquina2, dist, idc)
=======
	def agregar_calle(self, esquina1, esquina2):
		dist = esquina1.calcular_distancia(esquina2)
		self.mapa.agregar_arista(esquina1, esquina2, dist)
		self.cant_calles += 1
>>>>>>> .r10

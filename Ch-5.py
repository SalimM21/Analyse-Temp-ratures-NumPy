# Objectif : Filtrer un tableau NumPy en fonction de conditions multiples

# Créez un tableau NumPy avec des valeurs numériques variées
import numpy as np
data = np.array([10, 25, 30, 45, 50, 60, 75, 80])

# Utilisez numpy.where() pour sélectionner les éléments supérieurs à un certain seuil

seuil = 40
indices_sup_seuil = np.nonzero(data > seuil)
# Affichez les indices et les valeurs correspondantes
# print("Indices des éléments supérieurs à", seuil, ":", indices_sup_seuil[0])
print("Valeurs correspondantes :", data[indices_sup_seuil])

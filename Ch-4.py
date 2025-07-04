# Objectif : Effectuer des opérations sur des matrices en utilisant NumPy

# Créez deux matrices NumPy.
import numpy as np
matrice1 = np.array([[1, 2, 3], [4, 5, 6]])
matrice2 = np.array([[7, 8, 9], [10, 11, 12]])

# Effectuez une multiplication matricielle.
produit_matriciel = np.dot(matrice1, matrice2.T)
# Affichez le résultat de la multiplication matricielle.
print("Produit matriciel :")
print(produit_matriciel)

# Calculez la transposée et l'inverse de la matrice résultante

transpose = np.transpose(produit_matriciel)
inverse = np.linalg.inv(produit_matriciel)
# Affichez la transposée et l'inverse.
print("\nTransposée :")
print(transpose)
print("\nInverse :")
print(inverse)
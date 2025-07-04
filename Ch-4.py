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


print("\n--------------------------------------------------------------")


# Vérifiez que la multiplication de la matrice par son inverse donne la matrice identité.
identite = np.dot(produit_matriciel, inverse)
print("\nProduit de la matrice et de son inverse (doit être la matrice identité) :")
print(identite)
# Vérifiez que la transposée de la matrice est égale à l'inverse de la matrice transposée.
assert np.allclose(transpose, inverse.T), "La transposée n'est pas égale à l'inverse de la matrice transposée"
print("La transposée est égale à l'inverse de la matrice transposée.")

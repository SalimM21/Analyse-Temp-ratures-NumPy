# Objectif : Comparer deux tableaux NumPy et trouver les éléments qui diffèrent.

# Créez deux tableaux NumPy similaires avec de petites différences

import numpy as np
tableau1 = np.array([1, 2, 3, 4, 5])
tableau2 = np.array([1, 2, 3, 4, 6])

# Utilisez numpy.where() pour trouver les indices où les éléments diffèrent.

indices_diff = np.nonzero(tableau1 != tableau2)

# Affichez les indices et les valeurs correspondantes des deux tableaux.
print("Indices des éléments qui diffèrent :", indices_diff[0])
print("Valeurs dans tableau1 :", tableau1[indices_diff])
print("Valeurs dans tableau2 :", tableau2[indices_diff])

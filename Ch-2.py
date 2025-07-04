# Objectif : Normaliser un tableau de données pour qu'il ait une moyenne de 0 et un écart-type de 1.

# Créez un tableau NumPy.
import numpy as np
data = np.array([10, 20, 30, 40, 50])

# Soustrayez la moyenne et divisez par l'écart-type pour normaliser les données.

moyenne = np.mean(data)
ecart_type = np.std(data)
normalized_data = (data - moyenne) / ecart_type

# Affichez les données normalisées
print("Données normalisées :", normalized_data)
# Affichez la moyenne et l'écart-type pour vérification
print(f"Moyenne des données normalisées : {np.mean(normalized_data):.2f}")
print(f"Écart-type des données normalisées : {np.std(normalized_data):.2f}")
# Vérifiez que la moyenne est proche de 0 et l'écart-type proche de 1
assert np.isclose(np.mean(normalized_data), 0, atol=1e-2), "La moyenne n'est pas proche de 0"
assert np.isclose(np.std(normalized_data), 1, atol=1e-2), "L'écart-type n'est pas proche de 1"
print("La normalisation a été effectuée avec succès.")  


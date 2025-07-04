# Objectif : Analyser un tableau de températures journalières

# Créez un tableau NumPy avec des données de températures
import numpy as np
temperatures = np.array([15.5, 16.2, 14.8, 17.0, 18.5, 19.1, 20.0])

# Calculez la température moyenne, la médiane, et l'écart-type avec numpy.mean(), numpy.median() et numpy.std().
moyenne = np.mean(temperatures)
mediane = np.median(temperatures)
ecart_type = np.std(temperatures)

# Affichez les résultats
print(f"Température moyenne : {moyenne:.2f}°C")
print(f"Température médiane : {mediane:.2f}°C")
print(f"Écart-type des températures : {ecart_type:.2f}°C")


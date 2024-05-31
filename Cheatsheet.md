### Cheat Sheet Python

#### 1. **Bases**

**Variables et Types de Données**
```python
# Types de base
integer = 10                # entier
float_num = 10.5            # nombre flottant
string = "Hello, World!"    # chaîne de caractères
boolean = True              # booléen

# Collections
list_example = [1, 2, 3]          # liste
tuple_example = (1, 2, 3)         # tuple
dict_example = {"key": "value"}   # dictionnaire
set_example = {1, 2, 3}           # ensemble
```

**Opérations de base**
```python
# Mathématiques
addition = 5 + 2
soustraction = 5 - 2
multiplication = 5 * 2
division = 5 / 2
modulo = 5 % 2
exposant = 5 ** 2

# Concaténation de chaînes
greeting = "Hello" + " " + "World!"

# Opérateurs de comparaison
is_equal = (5 == 5)         # True
is_not_equal = (5 != 5)     # False
is_greater = (5 > 2)        # True
is_less = (5 < 2)           # False
```

**Conditions**
```python
if condition:
    # faire quelque chose
elif another_condition:
    # faire autre chose
else:
    # faire autre chose
```

**Boucles**
```python
# Boucle for
for i in range(5):
    print(i)

# Boucle while
i = 0
while i < 5:
    print(i)
    i += 1
```

**Fonctions**
```python
def ma_fonction(parametre):
    return parametre * 2

resultat = ma_fonction(5)  # 10
```

#### 2. **Collections et Manipulations**

**Listes**
```python
ma_liste = [1, 2, 3, 4, 5]

# Accès aux éléments
print(ma_liste[0])    # 1
print(ma_liste[-1])   # 5

# Tranches (slices)
print(ma_liste[1:3])  # [2, 3]

# Ajouter et supprimer des éléments
ma_liste.append(6)
ma_liste.remove(3)

# Compréhension de liste
carres = [x**2 for x in ma_liste]
```

**Dictionnaires**
```python
mon_dict = {"nom": "Alice", "age": 25}

# Accès aux valeurs
print(mon_dict["nom"])  # Alice

# Ajouter ou modifier une paire clé-valeur
mon_dict["age"] = 26

# Parcourir un dictionnaire
for key, value in mon_dict.items():
    print(key, value)
```

#### 3. **Fonctionnalités Avancées**

**Classes et Objets**
```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

personne1 = Personne("Alice", 25)
personne1.saluer()  # Bonjour, je m'appelle Alice et j'ai 25 ans.
```

**Gestion des Exceptions**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro.")
finally:
    print("Cette partie est toujours exécutée.")
```

**Modules et Bibliothèques**
```python
# Importer un module
import math
print(math.sqrt(16))  # 4.0

# Importer une fonction spécifique
from math import sqrt
print(sqrt(16))  # 4.0
```

**Lecture et Écriture de Fichiers**
```python
# Lecture d'un fichier
with open('fichier.txt', 'r') as file:
    contenu = file.read()

# Écriture dans un fichier
with open('fichier.txt', 'w') as file:
    file.write("Bonjour, monde!")
```

#### 4. **Outils et Bonnes Pratiques**

**Pip - Gestionnaire de Packages**
```bash
# Installer un package
pip install nom_du_package

# Liste des packages installés
pip list
```

**Environnements Virtuels**
```bash
# Créer un environnement virtuel
python -m venv mon_env

# Activer l'environnement virtuel
# Windows
mon_env\Scripts\activate
# MacOS/Linux
source mon_env/bin/activate

# Désactiver l'environnement virtuel
deactivate
```

**Tests Unités**
```python
import unittest

class TestMaFonction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(ma_fonction(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```


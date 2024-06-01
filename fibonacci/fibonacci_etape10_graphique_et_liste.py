import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# Codes de couleur ANSI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'


a = 0
b = 1
etape = 1
run = True
nbr = []
etapes = []
while run:
    c = b
    b = a + b
    print(f"{Colors.RED}étape:{Colors.RESET}", etape,
          f"{Colors.GREEN}nombre:{Colors.RESET}", b)
    a = c
    etapes.append(etape)  # Ajouter l'étape actuelle à la liste des étapes
    etape = etape + 1
    print()
    if etape == 11:
        run = False
    nbr.append(b)

plt.grid(True)
plt.plot(etapes, nbr)
plt.xlabel('étape', fontsize=14)
plt.ylabel('valeur', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Série de Fibonacci jusqu\'à l\'étape 10', fontsize=16)

# Ajuster les intervalles de la grille
plt.gca().xaxis.set_major_locator(
    MultipleLocator(1))  # Intervalle de 1 sur l'axe x
plt.gca().yaxis.set_major_locator(MultipleLocator(
    5))  # Intervalle de 10 sur l'axe y (ajuster selon les besoins)

plt.show()

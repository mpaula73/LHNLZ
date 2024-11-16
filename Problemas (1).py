from itertools import combinations
from Logica import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from types import MethodType

'''import json

with open('variables.json', 'r') as file:
    data = json.load(file)

Ni = data['Ni']
Nj = data['Nj']
I = data['I']
J = data['J']'''

def escribir_reinas(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = 'No h'
    else:
        atomo = literal
        neg = 'H'
    i, j  = self.unravel(atomo)
    return f"{neg}ay una reina en la casilla ({i},{j})"

def escribir(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = 'No h'
    else:
        atomo = literal
        neg = 'H'
    i, j  = self.unravel(atomo)
    return f"{neg}ay una reina en la casilla ({i},{j})"

def escribir_rejilla(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    n, x, y  = self.unravel(atomo)
    return f"El número {n}{neg} está en la casilla ({x},{y})"

class Reinas:
    def __init__(self, Ni, Nj):
        self.Ni = Ni
        self.Nj = Nj
        self.I = list(range(Ni))
        self.J = list(range(Nj))
        self.RenC = Descriptor([Ni, Nj])
        self.RenC.escribir = MethodType(escribir_reinas, self.RenC)
        r1 = self.regla1()
        r2 = self.regla2()
        r3 = self.regla3()
        r4 = self.regla4()
        self.reglas = [r1, r2, r3, r4]

    def regla1(self):
        formula3 = ''
        inicial3 = True

        for i in range(self.Ni):
            formula2 = ''
            inicial2 = True

            for j in range(self.Nj):
                formula1 = ''
                inicial1 = True
                otras_filas = [y for y in self.J if y != j]

                for k in otras_filas:
                    if inicial1:
                        formula1 = self.RenC.ravel([i, k])
                        inicial1 = False
                    else:
                        formula1 = "(" + formula1 + "O" + self.RenC.ravel([i, k]) + ")"
                formula1 = "(" + self.RenC.ravel([i, j]) + ">-" + formula1 + ")"
                if inicial2:
                    formula2 = formula1
                    inicial2 = False
                else:
                    formula2 = "(" + formula2 + "Y" + formula1 + ")"
            if inicial3:
                formula3 = formula2
                inicial3 = False
            else:
                formula3 = "(" + formula3 + "Y" + formula2 + ")"
        return formula3

    def regla2(self):
        formula3 = ''
        inicial3 = True
        for i in range(self.Ni):
            formula2 = ''
            inicial2 = True
            for j in range(self.Nj):
                formula1 = ''
                inicial1 = True
                otras_columnas = [x for x in self.I if x != i]
                for l in otras_columnas:
                    if inicial1:
                        formula1 = self.RenC.ravel([l, j])
                        inicial1 = False
                    else:
                        formula1 = "(" + formula1 + "O" + self.RenC.ravel([l, j]) + ")"
                formula1 = "(" + self.RenC.ravel([i, j]) + ">-" + formula1 + ")"
                if inicial2:
                    formula2 = formula1
                    inicial2 = False
                else:
                    formula2 = "(" + formula2 + "Y" + formula1 + ")"
            if inicial3:
                formula3 = formula2
                inicial3 = False
            else:
                formula3 = "(" + formula3 + "Y" + formula2 + ")"
        print(formula3)
        return formula3

    def regla3(self):
        formula3 = ''
        inicial3 = True
        for i in range(self.Ni):
            formula2 = ''
            inicial2 = True
            for j in range(self.Nj):
                formula1 = ''
                inicial1 = True
                diagonal = [(x, y) for x in self.I for y in self.J if
                            (((i, j) != (x, y)) and ((i + j == x + y) or (i - j == x - y)))]
                for d in diagonal:
                    u = d[0]
                    v = d[1]
                    if inicial1:
                        formula1 = self.RenC.ravel([u, v])
                        inicial1 = False
                    else:
                        formula1 = "(" + formula1 + "O" + self.RenC.ravel([u, v]) + ")"
                formula1 = "(" + self.RenC.ravel([i, j]) + ">-" + formula1 + ")"
                if inicial2:
                    formula2 = formula1
                    inicial2 = False
                else:
                    formula2 = "(" + formula2 + "Y" + formula1 + ")"
            if inicial3:
                formula3 = formula2
                inicial3 = False
            else:
                formula3 = "(" + formula3 + "Y" + formula2 + ")"
        print(formula3)
        return formula3

    def regla4(self):
        formula2 = ''
        inicial2 = True
        for i in self.I:
            formula1 = ''
            inicial1 = True
            for j in self.J:
                if inicial1:
                    formula1 = self.RenC.ravel([i, j])
                    inicial1 = False
                else:
                    formula1 = "(" + formula1 + "O" + self.RenC.ravel([i, j]) + ")"
            if inicial2:
                formula2 = formula1
                inicial2 = False
            else:
                formula2 = "(" + formula2 + "Y" + formula1 + ")"
        print(formula2)

        formula4 = ''
        inicial4 = True
        for j in self.J:
            formula3 = ''
            inicial3 = True
            for i in self.I:
                if inicial3:
                    formula3 = self.RenC.ravel([i, j])
                    inicial3 = False
                else:
                    formula3 = "(" + formula3 + "O" + self.RenC.ravel([i, j]) + ")"
            if inicial4:
                formula4 = formula3
                inicial4 = False
            else:
                formula4 = "(" + formula4 + "Y" + formula3 + ")"
        print(formula4)

        Otoria([formula2, formula4])

        return Otoria([formula2, formula4])

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox

    def visualizar(self, I):
        # Initialize the figure
        fig, axes = plt.subplots()
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)

        # Draw the chessboard
        step_x = 1. / self.Ni  # Horizontal step size
        step_y = 1. / self.Nj  # Vertical step size
        tangulos = []

        # Create light and dark squares on the board
        for i in range(self.Ni):
            for j in range(self.Nj):
                color = 'cornsilk' if (i + j) % 2 == 0 else 'lightslategrey'
                tangulos.append(patches.Rectangle((i * step_x, j * step_y), step_x, step_y, facecolor=color))

        # Create the grid lines
        for i in range(self.Ni + 1):
            locacion_x = i * step_x
            tangulos.append(patches.Rectangle((locacion_x, 0), 0.005, 1, facecolor='black'))  # Vertical lines

        for j in range(self.Nj + 1):
            locacion_y = j * step_y
            tangulos.append(patches.Rectangle((0, locacion_y), 1, 0.005, facecolor='black'))  # Horizontal lines

        for t in tangulos:
            axes.add_patch(t)

        # Load the knight image
        arr_img = plt.imread("img/reina.png", format='png')
        imagebox = OffsetImage(arr_img, zoom=1.1 /(self.Ni*self.Nj))
        imagebox.image.axes = axes

        # Create the directions for the image according to the literal
        direcciones = {}
        for i in range(self.Ni):
            for j in range(self.Nj):
                direcciones[(i, j)] = [i * step_x + step_x / 2, 1 - (j * step_y + step_y / 2)]

        for l in I:
            if I[l]:
                x, y = self.RenC.unravel(l)
                ab = AnnotationBbox(imagebox, direcciones[(x, y)], frameon=False)
                axes.add_artist(ab)

        plt.show()

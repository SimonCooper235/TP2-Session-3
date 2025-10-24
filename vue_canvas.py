from PyQt6.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from modele_integration import ModeleIntegration

class MPLCanvas(FigureCanvasQTAgg):
    __model : ModeleIntegration

    def __init__(self, model : ModeleIntegration):
        self.__fig, self.__ax = plt.subplots()
        super().__init__(self.__fig)

        self.__model = model
        self.__model.modelChanged.connect(self.dessiner)

    def dessiner(self):
        try :
            self.__ax.clear()
            f = self.__model.fonction
            if f :
                x = np.linspace(self.__model.borneInf, self.__model.borneSup, 1000)
                y= f(x)
                self.__ax.plot(x, y, color = "Black")
            self.__ax.axhline(y=0, color="Black")
            self.__ax.axvline(x=0, color="Black")
            self.draw()
        except Exception as e :
            QMessageBox.critical(self, "Erreur", "la fonction est invalide")

    def dessiner_integration(self):
        try :
            self.__ax.clear()
            f = self.__model.fonction
            if f :
                x_plot = np.linspace(self.__model.borneInf, self.__model.borneSup, 1000)
                x_rect = np.linspace(self.__model.borneInf, self.__model.borneSup, self.__model.nombreHorizontalSlider + 1)
                dx = (self.__model.borneSup - self.__model.borneInf) / self.__model.nombreHorizontalSlider

                if self.__model.gaucheCheckBox:
                    x_gauche = x_rect[:-1]
                    self.__ax.plot(x_plot, f(x_plot), color="Black")
                    self.__ax.bar(x_gauche, f(x_gauche), width = dx, edgecolor = "Green", align = 'edge', facecolor = "none", linewidth = 1)

                elif self.__model.droiteCheckBox:
                    x_droite = x_rect[1:]
                    self.__ax.plot(x_plot, f(x_plot), color="Black")
                    self.__ax.bar(x_droite, f(x_droite), width = -dx, edgecolor="Green", align='edge', facecolor = "none", linewidth = 1)

                else:
                    pass
            self.__ax.axhline(y=0, color = "Black")
            self.__ax.axvline(x=0, color="Black")
            self.draw()
        except Exception as e :
            QMessageBox.critical(self, "Erreur", "la somme de Riemann et/ou l'intintégration est invalide")

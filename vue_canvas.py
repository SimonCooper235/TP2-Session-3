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
            self.draw()
        except Exception as e :
            QMessageBox.critical(self, "Erreur", "la fonction est invalide")

    def dessiner_integration(self):
        try :
            self.__ax.clear()
            f = self.__model.fonction
            try:
                dx = (self.__model.borneInf - self.__model.borneSup) / self.__model.nombreHorizontalSlider
                print(dx)
            except ZeroDivisionError as e:
                print(e)
        except Exception as e :
            print(e)

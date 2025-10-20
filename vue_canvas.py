from matplotlib.backends.backend_template import FigureCanvas

from modele_integration import ModeleInetgration


class MPLCanvas(FigureCanvas):
    __model : ModeleInetgration

    def __init__(self):
        super().__init__()
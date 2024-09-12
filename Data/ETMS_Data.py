import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk

import pandas as pd
# Función para cargar datos
def cargar_datos(archivo, I):
    datos = pd.read_csv(archivo, skiprows=[1, 2], delimiter=';', header=0, index_col=0, parse_dates=True)
    return datos

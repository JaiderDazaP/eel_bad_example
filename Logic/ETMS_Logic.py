import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk

# Funciones de conversión
def microvolts_to_volts(microvolts):
    return microvolts / 1e6

def volts_to_ohms(voltage, Vref=0.79932, RV=10e3):
    return Vref * RV / (voltage - Vref)

def resistance_to_temperature(resistance):
    if resistance > 10e3:
        temperature = (-24536.24 + 0.02350289 * resistance * 100 + 0.000000001034084 * (resistance * 100) ** 2) / 100
    else:
        temperature = (-24564.58 + 0.02353718 * resistance * 100 + 0.000000001027502 * (resistance * 100) ** 2) / 100
    return temperature - 273.15

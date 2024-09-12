import eel
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
# Importa las funciones desde la capa de Data y Logic
from Data.ETMS_Data import cargar_datos
from Logic.ETMS_Logic import microvolts_to_volts, volts_to_ohms, resistance_to_temperature


# Funciones para graficar
def graficar_voltaje_vs_tiempo(datos):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    datos = datos.ffill()
    for columna in datos.columns:
        ax.plot(datos.index, datos[columna], label=columna)
    ax.set_title('Voltaje vs Tiempo')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Voltaje')
    ax.legend()
    return fig

def graficar_temperatura_vs_tiempo(temperaturas):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    temperaturas = temperaturas.ffill()
    for columna in temperaturas.columns:
        ax.plot(temperaturas.index, temperaturas[columna], label=columna)
    ax.set_title('Temperatura vs Tiempo')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Temperatura (°C)')
    ax.legend()
    return fig

def mostrar_graficas(self):
    archivo_predeterminado = "TEST_ACC_30_01_2022.csv"
    datos = cargar_datos(archivo_predeterminado, 100e-6)
    datos = datos.applymap(microvolts_to_volts)
    # Completar más tarde


def init_gui():
    eel.init('web')  # Apunta a la carpeta donde están los archivos web

# Función para cargar la página HTML correspondiente
@eel.expose
def load_page(page_name):
    file_path = f'web/Pages/{page_name}.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"<h1>{page_name.capitalize()} no encontrado</h1>"

def start_gui():
    eel.start('index.html', size=(1200, 800))  # Abre la ventana con tamaño fijo

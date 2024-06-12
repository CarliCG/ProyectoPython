import pandas as pd  # Importamos la librería pandas para análisis de datos
import os  # OS para interactuar con el sistema operativo
from tkinter import Tk, Label, Button, filedialog, messagebox
from src.decorators.decorators import timeit, logit  # Importamos los decoradores

df = None  # Variable global para almacenar los datos

@logit  # Añadimos el logging a la función
@timeit  # Medimos el tiempo de ejecución
def load_data(data_path):
    """Cargar datos desde CSV"""
    global df
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)  # Cargamos los datos del archivo CSV
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path)  # Cargamos los datos del archivo Excel
    else:
        raise ValueError("Unsupported file format")  # Error si el formato es incorrecto
    messagebox.showinfo("Info", "Data loaded successfully")  # Muestra un mensaje de éxito
    return df  # Devolvemos el DataFrame con los datos cargados

@logit  # Añadimos el logging a la función
@timeit  # Medimos el tiempo de ejecución
def clean_data(df):
    """Limpiamos los datos, es decir quitamos espacios, comas y acomodamos"""
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)  # Convertimos la columna de precio a float
    messagebox.showinfo("Info", "Data cleaned successfully")  # Muestra un mensaje de éxito
    return df  # Devolvemos el DataFrame con datos formateados

@logit  # Añadimos el logging a la función
@timeit  # Medimos el tiempo de ejecución
def analyze_data(df):
    """Realizamos análisis básico de datos"""
    analysis = df.describe()  # Resumen estadístico
    highest_price = df.nlargest(5, "price")  # Productos con precios más altos
    result = f"Basic data analysis:\n{analysis}\n\nProducts with highest price:\n{highest_price}"
    messagebox.showinfo("Analysis", result)  # Muestra el análisis en un mensaje
    return result

@logit  # Añadimos el logging a la función
@timeit  # Medimos el tiempo de ejecución
def save_clean_data(df, output_path):
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)  # Guarda datos en archivo CSV
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False)  # Guarda en archivo Excel
    else:
        raise ValueError("Unsupported file format")  # Lanzamos un error si el formato del archivo no es compatible
    messagebox.showinfo("Info", f"Clean data saved to {output_path}")  # Muestra un mensaje de éxito

def open_file_dialog():
    file_path = filedialog.askopenfilename()  # Abre un diálogo para seleccionar archivo
    if file_path:
        load_data(file_path)  # Carga los datos seleccionados

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])  # Diálogo para guardar archivo
    if file_path:
        save_clean_data(df, file_path)  # Guarda los datos limpios

def clean_and_analyze_data():
    global df
    if df is not None:
        df = clean_data(df)  # Limpia los datos
        analyze_data(df)  # Analiza los datos
    else:
        messagebox.showerror("Error", "No data loaded")  # Error si no hay datos cargados

def create_gui():
    root = Tk()  # Crea la ventana principal de Tkinter
    root.title("Data Analysis Tool")  # Título de la ventana

    Label(root, text="Data Analysis Tool", font=("Helvetica", 16)).pack(pady=10)  # Etiqueta de título

    Button(root, text="Load Data", command=open_file_dialog).pack(pady=5)  # Botón para cargar datos
    Button(root, text="Clean and Analyze Data", command=clean_and_analyze_data).pack(pady=5)  # Botón para limpiar y analizar datos
    Button(root, text="Save Clean Data", command=save_file_dialog).pack(pady=5)  # Botón para guardar datos limpios

    root.mainloop()  # Inicia el bucle principal de Tkinter

if __name__ == "__main__":
    create_gui()  # Llama a la función para crear la GUI

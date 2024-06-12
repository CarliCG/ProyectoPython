import pandas as pd  # Importar Pandas para el manejo de datos
import os  # Importar os para operaciones del sistema operativo
from tkinter import filedialog, messagebox  # Importar módulos de tkinter para la interfaz gráfica
from ttkbootstrap import Style  # Importar estilo para la interfaz gráfica
from ttkbootstrap.dialogs import Messagebox  # Importar diálogo de mensajes
from ttkbootstrap import Button, Label, Entry, Frame  # Importar elementos de la interfaz gráfica

# Constantes para rutas de archivos
DATA_PATH = "data/raw/products.csv"
OUTPUT_PATH = "data/processed/cleaned_products.csv"

df = None  # Variable global para almacenar los datos

def load_data(data_path):
    """Cargar datos desde CSV"""
    global df
    try:
        if data_path.endswith(".csv"):
            df = pd.read_csv(data_path)  # Cargar archivo CSV en DataFrame
        elif data_path.endswith(".xlsx"):
            df = pd.read_excel(data_path)  # Cargar archivo Excel en DataFrame
        else:
            raise ValueError("Unsupported file format")  # Levantar error si el formato de archivo no es compatible
        Messagebox.show_info("Data loaded successfully")  # Mostrar mensaje de éxito
        return df  # Retornar DataFrame cargado
    except Exception as e:
        Messagebox.show_error(f"Error loading data: {str(e)}")  # Mostrar mensaje de error si falla la carga de datos

def clean_data(df):
    """Limpiamos los datos"""
    try:
        df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)  # Limpiar columna de precios
        Messagebox.show_info("Data cleaned successfully")  # Mostrar mensaje de éxito
        return df  # Retornar DataFrame limpio
    except Exception as e:
        Messagebox.show_error(f"Error cleaning data: {str(e)}")  # Mostrar mensaje de error si falla la limpieza de datos

def analyze_data(df):
    """Realizamos análisis básico de datos"""
    try:
        analysis = df.describe()  # Realizar análisis estadístico básico
        highest_price = df.nlargest(5, "price")  # Encontrar los 5 productos más caros
        result = f"Basic data analysis:\n{analysis}\n\nProducts with highest price:\n{highest_price}"  # Construir resultado
        Messagebox.show_info("Analysis", result)  # Mostrar resultado en mensaje
        return result  # Retornar resultado del análisis
    except Exception as e:
        Messagebox.show_error(f"Error analyzing data: {str(e)}")  # Mostrar mensaje de error si falla el análisis de datos

def save_clean_data(df, output_path):
    """Guarda los datos limpios"""
    try:
        if output_path.endswith(".csv"):
            df.to_csv(output_path, index=False)  # Guardar DataFrame como archivo CSV
        elif output_path.endswith(".xlsx"):
            df.to_excel(output_path, index=False)  # Guardar DataFrame como archivo Excel
        else:
            raise ValueError("Unsupported file format")  # Levantar error si el formato de archivo no es compatible
        Messagebox.show_info(f"Clean data saved to {output_path}")  # Mostrar mensaje de éxito
    except Exception as e:
        Messagebox.show_error(f"Error saving data: {str(e)}")  # Mostrar mensaje de error si falla el guardado de datos

def open_file_dialog():
    """Abre un diálogo para seleccionar archivo"""
    file_path = filedialog.askopenfilename()  # Abrir diálogo para seleccionar archivo
    if file_path:
        load_data(file_path)  # Cargar datos si se selecciona un archivo

def save_file_dialog():
    """Diálogo para guardar archivo"""
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])  # Abrir diálogo para guardar archivo
    if file_path:
        save_clean_data(df, file_path)  # Guardar datos si se selecciona una ruta

def clean_and_analyze_data():
    """Limpia y analiza los datos"""
    global df
    if df is not None:
        df = clean_data(df)  # Limpiar datos
        analyze_data(df)  # Analizar datos
    else:
        Messagebox.show_error("No data loaded")  # Mostrar mensaje de error si no hay datos cargados

def create_gui():
    """Crea la interfaz gráfica"""
    style = Style(theme='cosmo')  # Establecer estilo de la interfaz gráfica
    root = style.master  # Crear ventana principal
    root.title("Data Analysis Tool")  # Establecer título de la ventana

    frame = Frame(root, padding=10)  # Crear marco en la ventana principal
    frame.pack(padx=10, pady=10, fill="x", expand=True)  # Empaquetar el marco

    Label(frame, text="Data Analysis Tool", font=("Helvetica", 16)).pack(pady=10)  # Agregar etiqueta al marco

    Button(frame, text="Load Data", command=open_file_dialog, bootstyle="primary").pack(pady=5, fill="x")  # Botón para cargar datos
    Button(frame, text="Clean and Analyze Data", command=clean_and_analyze_data, bootstyle="secondary").pack(pady=5, fill="x")  # Botón para limpiar y analizar datos
    Button(frame, text="Save Clean Data", command=save_file_dialog, bootstyle="success").pack(pady=5, fill="x")  # Botón para guardar datos limpios

    root.mainloop()  # Ejecutar bucle principal de la interfaz gráfica

if __name__=="__main__":
    create_gui()  # Crear interfaz gráfica al ejecutar el script
    os.makedirs("data/processed", exist_ok=True)  # Crear directorio para datos procesados
    df = load_data(DATA_PATH)  # Cargar datos desde archivo al inicio
    df = clean_data(df)  # Limpiar datos al inicio
    analyze_data(df)  # Analizar datos al inicio
    save_clean_data(df, OUTPUT_PATH)  # Guardar datos limpios al inicio

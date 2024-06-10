import pandas as pd #importamos panda libreria para analizar datos
import os #OS para interactuar con el sistema operativo

def load_data(data_path):
    """Cargar datos desde CSV"""
    if data_path.endswith(".csv"):
        df=pd.read_csv(data_path) #Cargamos los datos del archivo CSV
    elif data_path.endswith("xlsx"):
        df=pd.read_excel(data_path) #Cargamos los datos del archivo excel
    else:
        raise ValueError("Unsupported file format")#Error si el formato es incorrecto
    print("Data loaded successfully")#imprime mensaje indicando q los datos cargaron corectamente
    return df #Devolvemos el DataFrame con los datos cargados

def clean_data (df):
    """Limpiamos los datos, es decir quitamos espacion, comas y acomodamos"""
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float) #convertimos la columna de precio a float
    print("Data cleaned successfully")
    return df #devolvemos el data frame con datos formateados

def analyze_data(df):
    """Realizamos analisis basico de datos"""
    print("Basic data analysis:")
    print(df.describe())#imprime resumen estadistico
    print("\nProducts with highest price")#Encabezado precios mas alto
    highestPrice=df.nlargest(5,"price")
    print(highestPrice)#imprime el precio mas alto

def save_clean_data(df,outputh_path):
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path,index=False) #Guarda datos en archivo csv
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path, index=False)#Guarda en archivo excel
    else:
        raise ValueError("Unsupported file format") #Lanzamos un error si el formato del archivo no es compatible
    print(f"Clean data saved to {outputh_path}")

if __name__=="__main__": # permitimos que el script solo se ejecute en este archivo
    data_path="data/raw/products.csv" #Definimos la ruta del archivo sin expresar
    outputh_path="data/processed/cleaned_products.csv"#definimos la ruta del archivo de datos procesados

    df=load_data(data_path)# Cargar los datos de un archivo especifico
    df=clean_data(df)#Limpiamos los datos cargados
    df=analyze_data(df)#Analizis basico de la data
    os.makedirs("data/processed", exist_ok=True) #Directorio para los datos procesados

    save_clean_data(df,outputh_path)
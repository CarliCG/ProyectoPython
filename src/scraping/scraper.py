import requests # Importar el modulo request para solicitar http
from bs4 import BeautifulSoup # importamos BS para analizar HTML
import pandas as pd # Importamos pandas para manejar los datos en los dataframes

def fetch_page(url): #obtenemos contenido de la pag
    
    response = requests.get(url) #Solicitud GEt para la url
    if response.status_code == 200: #Status 200 es exitoso
        return response.content #si es exitosa devolvemos el contenido de la pagina
    else:
        raise Exception(f"Failed to fetch page: {url}")#excepcion por si la solicitud falla
    
def parse_product(product):
    """Analizamos detalles de un producto"""
    title= product.find("a",class_="title").text.strip() #encontramos y objetenmos el titulo del producto
    description=product.find("p",class_="description").text.strip()#descripcion del producto
    price=product.find("h4",class_="price").text.strip() # precio del producto

    return {
        "title": title,
        "description":description,
        "price":price,
    }

def scrape(url):
    """Funcion principal de scraping"""
    page_content = fetch_page(url) #obtener codigo base de la pagina
    soup=BeautifulSoup(page_content, "html.parser") # analizamos la pagina con SP
    products=soup.find_all("div",class_="thumbnail") # encontramos todos los div "thumnail" que representa productos
    
    #guardamos los productos en una lista para almacenar los datos del producto
    products_data=[]
    for product in products:
        product_info=parse_product(product)
        products_data.append(product_info)
    
    return pd.DataFrame(products_data)
#Definimos url base para el; scraping
base_url="https://webscraper.io/test-sites/e-commerce/allinone"

#llamamos la funcion scrape para obtener datosd el producto

df=scrape(base_url)

#imprimimos el df (dataframe)resultante

print (df)
#guardamos datos de un archivo csv sin incluir el indice

df.to_csv("data/raw/products.csv", index=False)#guardamos los datos en un archivo csv
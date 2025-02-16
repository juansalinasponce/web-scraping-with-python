import requests
from bs4 import BeautifulSoup

# URL de la página a scrapear
url = "https://juansalinasponce.github.io/"

# Realizar la solicitud HTTP
response = requests.get(url)
print(response)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    
    # Extraer información deseada
    nombre = soup.find('h1').text.strip()
    print(nombre)
    """
    linkedin = soup.find('a', href=True).text.strip()
    perfil_profesional = soup.find('h2', text='Perfil Profesional').find_next('p').text.strip()
    
    # Imprimir resultados
    print("Nombre:", nombre)
    print("LinkedIn:", linkedin)
    print("Perfil Profesional:", perfil_profesional)
else:
    print("Error al acceder a la página:", response.status_code)

    """
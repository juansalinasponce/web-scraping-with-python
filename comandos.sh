#Instala virtualenv usando pip. Si no tienes pip instalado, 
#primero asegúrate de tener Python instalado. Luego, 
#ejecuta el siguiente comando:
pip install virtualenv

#Verifica la instalación ejecutando:
virtualenv --version

#En Macos

virtualenv venv_scraper

#activar

source venv_scraper/bin/activate


#Activar en windows

venv_scraper\Scripts\activate

#Desactivar
deactivate

#Instalar librerías

pip install -r requirements.txt
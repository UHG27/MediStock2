from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar el servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Crear opciones para Chrome
options = webdriver.ChromeOptions()

# Iniciar el navegador con las opciones y el servicio configurado
driver = webdriver.Chrome(service=service, options=options)

# Abre una página web
driver.get("https://www.google.com")

# Cierra el navegador
driver.quit()

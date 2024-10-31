from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Extiende de LiveServerTestCase para realizar pruebas en un servidor de desarrollo Django.
class ProductTestCase(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #Inicia el navegador Chrome antes de las pruebas.
        cls.driver = webdriver.Chrome()
        
    @classmethod
    def tearDownClass(cls):
        # Cierra el navegador después de las pruebas
        cls.driver.quit()
        super().tearDownClass()
    
    def test_create_product(self):
        # Abre la pagina de creacion de productos
        self.driver.get(f'{self.live_server_url}/registrarProducto')
        
        # Aqui, encuentra los campos del formulario y completa con datos.
        nombre_input = self.driver.find_element(By.ID, 'txtNombre')
        descripcion_input = self.driver.find_element(By.ID, 'txtDescripcion')
        precio_input = self.driver.find_element(By.ID, 'numPrecio')
        stock_input = self.driver.find_element(By.ID, 'numStock')
        fecha_input = self.driver.find_element(By.ID, 'txtFechaDeCreacion')
        
        # Se completan los campos con datos validos de prueba.
        nombre_input.send_keys('Ibuprofeno')
        descripcion_input.send_keys('alivia el dolor y baja la fiebre')
        precio_input.send_keys('35.99')
        stock_input.send_keys('13')
        fecha_input.send_keys('2024-10-23')
        
        # Se envian los datos.
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Tiempo para que el navegador procese los datos.
        time.sleep(5)
        
        self.assertIn('Ibuprofeno', self.driver.page_source)
        
    def test_edit_product(self):
        # Aqui se abrira la pagina de edicion del producto.
        self.driver.get(f'{self.live_server_url}/edicionProducto/Ibuprofeno')
        
        # Encontrara los campos del formulario y completara con los nuevos datos.
        nombre_input = self.driver.find_element(By.ID, 'txtNombre')
        descripcion_input = self.driver.find_element(By.ID, 'txtDescripcion')
        precio_input = self.driver.find_element(By.ID, 'numPrecio')
        
        # Aqui limpia y actualiza los campos
        nombre_input.clear()
        nombre_input.send_keys('IbuCompuesto')
        descripcion_input.clear()
        descripcion_input.send_keys('Antiinflamatorio, que ayuda a aliviar dolores comunes de gripe')
        precio_input.clear()
        precio_input.send_keys('38.50')
        
        # Envia los datos actualizados
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit]")
        submit_button.click()
        
        # Tiempo para que el navegador procese los datos.
        time.sleep(5)
        
        self.assertIn('IbuCompuesto', self.driver.page_source)
        
    def test_delete_product(self):
        # Abre la página principal donde está el listado de productos.
        self.driver.get(f'{self.live_server_url}/')
        
        # Busca el botón de eliminar para el producto
        delete_button = self.driver.find_element(By.LINK_TEXT, 'Eliminar')
        
        delete_button.click()
        
        time.sleep(5)
        
        self.assertNotIn('IbuCompuesto', self.driver.page_source)
       
        
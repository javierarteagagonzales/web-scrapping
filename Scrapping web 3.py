import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# configurar el controlador de Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# navegar a la página web
url = 'https://twitter.com/search?q=javascript&src=typed_query'
driver.get(url)

# maximizar la ventana del navegador
driver.maximize_window()

# esperar 15 segundos para permitir que la página cargue completamente
time.sleep(15)

# encontrar todos los elementos que coinciden con el XPath dado
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@lang]'))
)

# extraer el contenido de los elementos y guardarlo en una lista
content = [element.text for element in elements]

# imprimir la lista que contiene el contenido extraído
print(content)

# cerrar el controlador de Chrome
driver.quit()

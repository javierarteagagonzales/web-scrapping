import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# configurar el controlador de Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# navegar a la página web
url = 'https://www.amazon.com/s?k=tech+books&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1'
driver.get(url)

# esperar 5 segundos para permitir que la página cargue completamente
time.sleep(5)

# encontrar todos los elementos que coinciden con el XPath dado
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
)

# extraer el contenido de los elementos y guardarlo en una lista
content = [element.text for element in elements]

# imprimir la lista que contiene el contenido extraído
print(content)

# cerrar el controlador de Chrome
driver.quit()

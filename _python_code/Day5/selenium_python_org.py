from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time_module

# Iniciar el navegador
browser = webdriver.Chrome()
browser.get("https://www.python.org")

# Encontrar elementos
event_times = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time, name in zip(event_times, event_names):
    print(time.text, name.text)

# Esperar 3 segundos antes de cerrar
time_module.sleep(3)

browser.quit()
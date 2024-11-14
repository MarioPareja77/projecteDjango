from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

def test_login(self):
    # Anem a la pàgina de login de l'administració
    self.selenium.get(f'{self.live_server_url}/admin/login/')

    # Comprovem que el títol de la pàgina és el que esperem
    self.assertEqual(self.selenium.title, "Log in | Django site admin")

    # Introduïm les credencials i fem clic a "Log in"
    username_input = self.selenium.find_element(By.NAME, "username")
    username_input.send_keys('isard')
    password_input = self.selenium.find_element(By.NAME, "password")
    password_input.send_keys('pirineus')

    # Enviem el formulari
    login_button = self.selenium.find_element(By.XPATH, '//input[@value="Log in"]')
    login_button.send_keys(Keys.RETURN)

    # Esperem explícitament que el títol de la pàgina sigui el que esperem
    WebDriverWait(self.selenium, 3).until(
        EC.title_contains("Site administration")
    )

    # Verifiquem si hem iniciat sessió correctament
    self.assertEqual(self.selenium.title, "Site administration | Django site admin")
    self.assertIn('/admin/', self.selenium.current_url)

    # Anem a la pàgina per afegir un nou usuari
    self.selenium.get(f'{self.live_server_url}/admin/auth/user/add/')

    # Comprovem que el títol de la pàgina és el que esperem per a la creació d'un usuari
    self.assertEqual(self.selenium.title, "Add user | Django site admin")

    # Introduïm les dades pel nou usuari
    username_input = self.selenium.find_element(By.NAME, "username")
    username_input.send_keys("mparejanieto")
    password1_input = self.selenium.find_element(By.NAME, "password1")
    password1_input.send_keys("1234")
    password2_input = self.selenium.find_element(By.NAME, "password2")
    password2_input.send_keys("1234")

    # Guardem el nou usuari fent clic al botó "Save"
    save_button = self.selenium.find_element(By.NAME, "_save")
    save_button.click()

    # Esperem que la pàgina de confirmació o la llista d'usuaris es carregui
    WebDriverWait(self.selenium, 10).until(
        EC.title_contains("Select user to change")
    )

    # Verifiquem que estem a la pàgina de selecció d'usuaris
    self.assertEqual(self.selenium.title, "Select user to change | Django site admin")

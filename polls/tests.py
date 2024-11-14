from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

def test_login(self):
    # Vamos a la página de login del admin
    self.selenium.get(f'{self.live_server_url}/admin/login/')

    # Comprobamos que el título de la página es el esperado
    self.assertEqual(self.selenium.title, "Log in | Django site admin")

    # Introducimos las credenciales y hacemos clic en "Log in"
    username_input = self.selenium.find_element(By.NAME, "username")
    username_input.send_keys('isard')
    password_input = self.selenium.find_element(By.NAME, "password")
    password_input.send_keys('pirineus')

    # Enviar el formulario
    login_button = self.selenium.find_element(By.XPATH, '//input[@value="Log in"]')
    login_button.send_keys(Keys.RETURN)

    # Esperamos explícitamente a que el título de la página sea el esperado
    WebDriverWait(self.selenium, 3).until(
        EC.title_contains("Site administration")
    )

    # Verificamos si hemos iniciado sesión correctamente
    self.assertEqual(self.selenium.title, "Site administration | Django site admin")
    self.assertIn('/admin/', self.selenium.current_url)

    # Navegamos a la página para añadir un nuevo usuario
    self.selenium.get(f'{self.live_server_url}/admin/auth/user/add/')

    # Comprobamos que el título de la página es el esperado para la creación de usuario
    self.assertEqual(self.selenium.title, "Add user | Django site admin")

    # Introducimos los datos para el nuevo usuario
    username_input = self.selenium.find_element(By.NAME, "username")
    username_input.send_keys("mparejanieto")
    password1_input = self.selenium.find_element(By.NAME, "password1")
    password1_input.send_keys("1234")
    password2_input = self.selenium.find_element(By.NAME, "password2")
    password2_input.send_keys("1234")

    # Guardamos el nuevo usuario haciendo clic en el botón "Save"
    save_button = self.selenium.find_element(By.NAME, "_save")
    save_button.click()

    # Esperamos que la página de confirmación o la lista de usuarios cargue
    WebDriverWait(self.selenium, 10).until(
        EC.title_contains("Select user to change")
    )

    # Verificamos que estamos en la página de selección de usuarios
    self.assertEqual(self.selenium.title, "Select user to change | Django site admin")

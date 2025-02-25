# CT-001-login.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAutenticacao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes"""
        print("\nIniciando testes de autenticação...")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 15)

    def setUp(self):
        """Preparação antes de cada teste"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )

    def test_1_login_sucesso(self):
        """CT-001: Login com credenciais válidas"""
        print("\nExecutando CT-001: Login válido...")
        self.driver.find_element(By.ID, "username").send_keys("jhenikbrito")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        self.assertIn("You logged into a secure area!", mensagem.text)
        print("✓ CT-001: Login válido - Aprovado")

    def test_2_login_falha(self):
        """CT-002: Login com credenciais inválidas"""
        print("\nExecutando CT-002: Login inválido...")
        self.driver.find_element(By.ID, "username").send_keys("jhenikbrito")
        self.driver.find_element(By.ID, "password").send_keys("senhaerrada")
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )
        self.assertIn("Your password is invalid!", mensagem.text)
        print("✓ CT-002: Login inválido - Aprovado")

    def test_3_logout(self):
        """CT-003: Logout após login bem-sucedido"""
        print("\nExecutando CT-003: Logout...")
        self.driver.find_element(By.ID, "username").send_keys("jhenikbrito")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        btn_logout = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))
        )
        btn_logout.click()

        mensagem = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        self.assertIn("You logged out", mensagem.text)
        print("✓ CT-003: Logout - Aprovado")

    @classmethod
    def tearDownClass(cls):
        """Finalização dos testes"""
        print("\nFinalizando todos os testes...")
        cls.driver.quit()
        print("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
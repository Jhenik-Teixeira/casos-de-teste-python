# DOCUMENTO DE CASO DE TESTE: CASOTESTE-005-formularios.pdf
# Testes de caixinhas de seleção 

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FillingOutFormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        """Abre a página de preenchimento de formulários"""
        self.driver.get("https://ultimateqa.com/filling-out-forms/")
        self.wait.until(EC.presence_of_element_located((By.ID, "et_pb_contact_form_0")))

    def fill_form(self, name, message):
        """Preenche o formulário com nome e mensagem"""
        self.driver.find_element(By.ID, "et_pb_contact_name_0").send_keys(name)
        self.driver.find_element(By.ID, "et_pb_contact_message_0").send_keys(message)

    def submit_form(self):
        """Submete o formulário"""
        self.driver.find_element(By.CSS_SELECTOR, "button.et_pb_contact_submit").click()

    def get_success_message(self):
        """Retorna a mensagem de sucesso após o envio do formulário"""
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.et_pb_contact_form_0 div.et-pb-contact-message"))
        ).text

    def get_error_message(self):
        """Retorna a mensagem de erro quando o formulário é enviado sem dados"""
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.et_pb_contact_form_0 div.et-pb-contact-message"))
        ).text

class TestFillingOutForms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes"""
        logger.info("\nIniciando testes de preenchimento de formulários...")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def setUp(self):
        """Preparação antes de cada teste"""
        self.forms_page = FillingOutFormsPage(self.driver)
        self.forms_page.open()

    def test_1_envio_correto(self):
        """CASOTESTE-001: Envio correto do formulário"""
        logger.info("\nExecutando CASOTESTE-001: Envio correto do formulário...")
        self.forms_page.fill_form("João Silva", "Esta é uma mensagem de teste.")
        self.forms_page.submit_form()

        success_message = self.forms_page.get_success_message()
        self.assertIn("Thanks for contacting us", success_message)
        logger.info("✓ CASOTESTE-001: Formulário enviado com sucesso - Aprovado")

    def test_2_envio_dados_ausentes(self):
        """CASOTESTE-002: Envio do formulário com dados ausentes"""
        logger.info("\nExecutando CASOTESTE-002: Envio do formulário com dados ausentes...")
        self.forms_page.submit_form()

        error_message = self.forms_page.get_error_message()
        self.assertIn("Please, fill in the following fields:", error_message)
        logger.info("✓ CASOTESTE-002: Mensagem de erro exibida corretamente - Aprovado")

    @classmethod
    def tearDownClass(cls):
        """Finalização dos testes"""
        logger.info("\nFinalizando todos os testes...")
        cls.driver.quit()
        logger.info("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
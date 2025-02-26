# DOCUMENTO DE CASO DE TESTE: CASOTESTE-004-caixaDESelecao.pdf
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

class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        """Abre a página de checkboxes"""
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        self.wait.until(EC.presence_of_element_located((By.ID, "checkboxes")))

    def get_checkboxes(self):
        """Retorna todas as caixas de seleção"""
        return self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    def is_checkbox_checked(self, checkbox):
        """Verifica se uma caixa de seleção está marcada"""
        return checkbox.is_selected()

    def toggle_checkbox(self, checkbox):
        """Alterna o estado de uma caixa de seleção (marca/desmarca)"""
        checkbox.click()

class TestCheckboxes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes"""
        logger.info("\nIniciando testes de checkboxes...")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def setUp(self):
        """Preparação antes de cada teste"""
        self.checkboxes_page = CheckboxesPage(self.driver)
        self.checkboxes_page.open()

    def test_1_verificar_checkboxes(self):
        """CASOTESTE-001: Verificar se as checkboxes estão presentes"""
        logger.info("\nExecutando CASOTESTE-001: Verificar checkboxes...")
        checkboxes = self.checkboxes_page.get_checkboxes()
        self.assertEqual(len(checkboxes), 2, "Deve haver 2 checkboxes na página")
        logger.info("✓ CASOTESTE-001: Checkboxes presentes - Aprovado")

    def test_2_desmarcar_checkboxes(self):
        """CASOTESTE-002: Desmarcar checkboxes que estão marcadas"""
        logger.info("\nExecutando CASOTESTE-002: Desmarcar checkboxes...")
        checkboxes = self.checkboxes_page.get_checkboxes()

        for checkbox in checkboxes:
            if self.checkboxes_page.is_checkbox_checked(checkbox):
                self.checkboxes_page.toggle_checkbox(checkbox)
                self.assertFalse(
                    self.checkboxes_page.is_checkbox_checked(checkbox),
                    "Checkbox deveria estar desmarcada"
                )
        logger.info("✓ CASOTESTE-002: Checkboxes desmarcadas - Aprovado")

    def test_3_marcar_checkboxes(self):
        """CASOTESTE-003: Marcar checkboxes que estão desmarcadas"""
        logger.info("\nExecutando CASOTESTE-003: Marcar checkboxes...")
        checkboxes = self.checkboxes_page.get_checkboxes()

        for checkbox in checkboxes:
            if not self.checkboxes_page.is_checkbox_checked(checkbox):
                self.checkboxes_page.toggle_checkbox(checkbox)
                self.assertTrue(
                    self.checkboxes_page.is_checkbox_checked(checkbox),
                    "Checkbox deveria estar marcada"
                )
        logger.info("✓ CASOTESTE-003: Checkboxes marcadas - Aprovado")

    @classmethod
    def tearDownClass(cls):
        """Finalização dos testes"""
        logger.info("\nFinalizando todos os testes...")
        cls.driver.quit()
        logger.info("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
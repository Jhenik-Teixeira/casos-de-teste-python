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

class FloatingMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        """Abre a página do menu flutuante"""
        self.driver.get("https://the-internet.herokuapp.com/floating_menu")
        self.wait.until(EC.presence_of_element_located((By.ID, "menu")))

    def is_menu_visible(self):
        """Verifica se o menu está visível"""
        return self.driver.find_element(By.ID, "menu").is_displayed()

    def scroll_page(self, pixels):
        """Rola a página para baixo por um número específico de pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

class TestFloatingMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes"""
        logger.info("\nIniciando testes do menu flutuante...")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def setUp(self):
        """Preparação antes de cada teste"""
        self.menu_page = FloatingMenuPage(self.driver)
        self.menu_page.open()

    def test_1_menu_visible(self):
        """CASOTESTE-006-01: Verificar se o menu está visível"""
        logger.info("\nExecutando CASOTESTE-006-01: Verificar visibilidade do menu...")
        self.assertTrue(self.menu_page.is_menu_visible(), "O menu deve estar visível")
        logger.info("✓ CASOTESTE-006-01: Menu visível - Aprovado")

    def test_2_menu_stays_visible_after_scroll(self):
        """CASOTESTE-006-02: Verificar se o menu permanece visível após rolar a página"""
        logger.info("\nExecutando CASOTESTE-006-02: Verificar visibilidade do menu após rolagem...")
        self.menu_page.scroll_page(500)  # Rola a página 500 pixels
        self.assertTrue(self.menu_page.is_menu_visible(), "O menu deve permanecer visível após rolar a página")
        logger.info("✓ CASOTESTE-006-02: Menu permanece visível após rolagem - Aprovado")

    @classmethod
    def tearDownClass(cls):
        """Finalização dos testes"""
        logger.info("\nFinalizando todos os testes...")
        cls.driver.quit()
        logger.info("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
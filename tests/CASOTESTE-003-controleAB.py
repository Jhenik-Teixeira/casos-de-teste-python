# DOCUMENTO DE CASO DE TESTE: CASOTESTE-003.pdf
# Teste de Controle A/B

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestABTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes."""
        print("\nIniciando testes de Controle A/B...")
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def setUp(self):
        """Preparação antes de cada teste."""
        self.driver.get("https://the-internet.herokuapp.com/abtest")
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )

    def test_1_verificar_versao_ab(self):
        """CASOTESTE-003-01: Verificar se a página exibe uma das versões (A ou B)."""
        print("\nExecutando CASOTESTE-003-01: Verificar versão A/B...")
        
        # Verifica o título da página
        titulo = self.driver.find_element(By.TAG_NAME, "h3").text
        self.assertIn("A/B Test", titulo)
        print(f"✓ Título da página: {titulo}")

        # Verifica o texto da página
        texto = self.driver.find_element(By.TAG_NAME, "p").text
        if "teste de divisão" in texto.lower() or "split testing" in texto.lower():
            print(f"✓ Texto exibido: {texto}")
        else:
            self.fail("Texto da página não corresponde ao esperado.")

    @classmethod
    def tearDownClass(cls):
        """Limpeza após todos os testes."""
        print("\nFinalizando testes de Controle A/B...")
        cls.driver.quit()
        print("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
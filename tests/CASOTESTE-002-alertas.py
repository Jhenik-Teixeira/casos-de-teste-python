# DOCUMENTO DE CASO DE TESTE: CASOTESTE-003.pdf
# Testes de Alertas e Pop-ups

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAlertas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial antes dos testes."""
        print("\nIniciando testes de alertas e pop-ups...")
        service = Service(ChromeDriverManager().install())  # Configuração automática do ChromeDriver
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def setUp(self):
        """Preparação antes de cada teste."""
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Click for JS Alert']"))
        )

    def test_1_alerta_simples(self):
        """CASOTESTE-003-01: Teste de alerta JavaScript simples."""
        print("\nExecutando CASOTESTE-003-01: Alerta simples...")  # CORRIGIDO AQUI
        
        # Clica no botão que gera o alerta
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        
        # Aguarda o alerta e aceita
        alerta = self.wait.until(EC.alert_is_present())
        alerta.accept()
        
        # Verifica a mensagem de resultado
        resultado = self.driver.find_element(By.ID, "result").text
        self.assertEqual("You successfully clicked an alert", resultado)
        print("✓ CASOTESTE-003-01: Alerta simples tratado com sucesso")

    def test_2_alerta_confirmacao(self):
        """CASOTESTE-003-02: Teste de alerta com confirmação."""
        print("\nExecutando CASOTESTE-003-02: Alerta de confirmação...")
        
        # Clica no botão que gera o alerta de confirmação
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        
        # Aguarda o alerta e confirma
        alerta = self.wait.until(EC.alert_is_present())
        alerta.accept()
        
        # Verifica a mensagem de resultado
        resultado = self.driver.find_element(By.ID, "result").text
        self.assertEqual("You clicked: Ok", resultado)
        print("✓ CASOTESTE-003-02: Alerta de confirmação aceito")
        
        # Testa cancelamento
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alerta = self.wait.until(EC.alert_is_present())
        alerta.dismiss()
        
        resultado = self.driver.find_element(By.ID, "result").text
        self.assertEqual("You clicked: Cancel", resultado)
        print("✓ CASOTESTE-003-02: Alerta de confirmação cancelado")

    def test_3_alerta_prompt(self):
        """CASOTESTE-003-03: Teste de alerta com prompt."""
        print("\nExecutando CASOTESTE-003-03: Alerta com prompt...")
        
        # Clica no botão que gera o prompt
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        
        # Aguarda o prompt, insere texto e aceita
        alerta = self.wait.until(EC.alert_is_present())
        texto_teste = "Teste Automatizado"
        alerta.send_keys(texto_teste)
        alerta.accept()
        
        # Verifica se o texto foi capturado corretamente
        resultado = self.driver.find_element(By.ID, "result").text
        self.assertEqual(f"You entered: {texto_teste}", resultado)
        print("✓ CASOTESTE-003-03: Prompt preenchido e confirmado com sucesso")

    @classmethod
    def tearDownClass(cls):
        """Limpeza após todos os testes."""
        print("\nFinalizando testes de alertas...")
        cls.driver.quit()
        print("Testes concluídos com sucesso!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
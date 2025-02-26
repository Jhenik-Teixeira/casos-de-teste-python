## 🚀 Testes Automatizados com Selenium e Python

Projeto de testes automatizados para validar funcionalidades em páginas web usando Selenium e Python.

## 🛠 Como Executar

### 1. Pré-requisitos
- **Python 3.8+**: Instale o Python.
- **Google Chrome**: Baixe o Chrome.

### 2. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 3. Configure o Ambiente Virtual (Opcional)
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 4. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 5. Execute os Testes

#### Todos os testes:
```bash
python -m unittest discover
```

#### Teste específico (ex: menu flutuante):
```bash
python tests/CASOTESTE-006-menu.py
```

## 🧬 Estrutura do Projeto
```
seu-repositorio/
├── tests/                  
│   ├── testes.py 
├── docs/
│   ├── documentos.pdf  
└── README.md               
```

## 📝 Dependências
- **Selenium**: Automação de navegadores.
- **WebDriver Manager**: Gerencia o WebDriver do Chrome.
- **Unittest**: Framework de testes do Python.

Instale tudo com:
```bash
pip install -r requirements.txt
```

## 🤝 Contribuição
1. Faça um **fork** do repositório.
2. Crie uma **branch** (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

## 💎 Contato
- **Nome:** Jhenik Teixeira
- **E-mail:** jheniktbrito@gmail.com
- **GitHub:** jhenik-teixeira

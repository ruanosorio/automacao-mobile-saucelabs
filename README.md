# Automação Mobile - SauceLabs

Projeto de automação de testes mobile usando Python, Pytest, Appium e Page Object Model.

## Tecnologias

- **Python** 3.10+
- **Pytest** - Framework de testes
- **Appium** - Automação mobile
- **Page Object Model** - Padrão de design
- **Allure** - Relatórios

## Pré-requisitos

- Python >= 3.10
- Node.js e npm
- Appium Server
- Android Studio/ADB

## Instalação

```bash
# Clone o repositório
git clone <repo-url>

# Instale as dependências
pip install -r requirements.txt
```

## Estrutura

```
├── apk/                    # APK para testes
├── config/                 # Configurações
├── factories/              # Factory Pattern
├── pages/                  # Page Object Model
├── tests/                  # Casos de teste
├── utils/                  # Utilitários
├── reports/                # Relatórios Allure
├── conftest.py             # Configurações Pytest
└── pytest.ini             # Configurações Pytest
```

## Execução

```bash
# Todos os testes
pytest tests/

# Testes específicos
pytest tests/test_login.py
pytest tests/test_hiring_products.py

# Com relatório Allure
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results

# Em paralelo
pytest tests/ -n auto
```

## Relatórios

Os relatórios Allure são gerados em `reports/allure-results/`

## Arquitetura

- **Page Object Model**: Cada página é uma classe com localizadores e métodos
- **Factory Pattern**: Criação centralizada de objetos de teste
- **Base Page**: Métodos comuns compartilhados entre páginas
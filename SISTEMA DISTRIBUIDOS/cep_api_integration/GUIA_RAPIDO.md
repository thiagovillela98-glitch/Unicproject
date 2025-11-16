# ⚡ Guia Rápido de Uso

## 🚀 Instalação em 3 Passos

### 1️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure seu token
Edite o arquivo `config.py` e coloque seu token:
```python
API_TOKEN = "seu_token_aqui"
```

💡 **Obtenha um token grátis em:** https://www.cepaberto.com/

### 3️⃣ Teste a instalação
```bash
python teste_rapido.py
```

---

## 💻 Como Executar

### Opção 1: Programa Principal (Recomendado)
```bash
python main.py
```

Menu interativo com todas as funcionalidades:
- Buscar CEP individual
- Buscar múltiplos CEPs
- Buscar capitais
- Buscar por região
- Ver histórico e estatísticas

### Opção 2: Exemplos de Demonstração
```bash
python exemplos.py
```

6 exemplos prontos para você testar:
1. Busca simples
2. Múltiplos CEPs
3. Validação de dados
4. Exportação (JSON/CSV)
5. CEPs por estado
6. Tratamento de erros

---

## 📖 Uso no Código

### Exemplo Simples
```python
from cep_api import CepAbertoAPI
from config import API_TOKEN

# Inicializa
api = CepAbertoAPI(token=API_TOKEN)

# Busca um CEP
resultado = api.buscar_cep("01001000")

# Exibe resultado
if resultado:
    print(f"{resultado['logradouro']}, {resultado['bairro']}")
    print(f"{resultado['cidade']['nome']}/{resultado['estado']['sigla']}")
```

### Buscar Vários CEPs
```python
ceps = ["01001000", "20040020", "30130100"]
resultados = api.buscar_multiplos_ceps(ceps)
print(f"Encontrados: {len(resultados)} CEPs")
```

### Exportar Resultados
```python
api.exportar_resultados(resultados, "meus_ceps.json")
```

---

## 🎯 CEPs para Testar

### Capitais
- **São Paulo/SP:** 01001-000
- **Rio de Janeiro/RJ:** 20040-020
- **Belo Horizonte/MG:** 30130-100
- **Salvador/BA:** 40020-000
- **Brasília/DF:** 70040-902

### Regiões
- **Sudeste:** 01001000, 20040020, 30130100
- **Sul:** 80010000, 90010000, 88010000
- **Nordeste:** 40020000, 50010000, 60010000
- **Norte:** 69005000, 66010000, 78010000
- **Centro-Oeste:** 70040902, 74003010, 79002000

---

## ❓ Problemas Comuns

### ❌ Erro de Autenticação
**Solução:** Verifique se o token está correto em `config.py`

### ❌ CEP Não Encontrado
**Solução:** Confirme se o CEP existe e está no formato correto (8 dígitos)

### ❌ Timeout
**Solução:** Verifique sua conexão com internet

### ❌ Limite de Requisições
**Solução:** Aguarde algumas horas ou faça upgrade do plano

---

## 📚 Documentação Completa

Para mais informações, consulte o arquivo `README.md` completo.

---

## 🎓 Estrutura do Projeto

```
cep_api_integration/
├── cep_api.py           ← Classe principal
├── main.py              ← Programa interativo
├── exemplos.py          ← Exemplos de uso
├── teste_rapido.py      ← Teste de instalação
├── config.py            ← Configuração (token)
├── requirements.txt     ← Dependências
└── README.md           ← Documentação completa
```

---

## ✅ Checklist de Uso

- [ ] Instalei as dependências (`pip install -r requirements.txt`)
- [ ] Configurei meu token em `config.py`
- [ ] Executei o teste rápido (`python teste_rapido.py`)
- [ ] Testei o programa principal (`python main.py`)
- [ ] Explorei os exemplos (`python exemplos.py`)
- [ ] Li a documentação completa (`README.md`)

---

## 🎯 Pronto para Apresentar!

Este projeto está completo e pronto para ser apresentado como trabalho de faculdade sobre **Validação e Integração entre APIs**.

### Principais Destaques:
✅ Integração com API REST  
✅ Validação de dados  
✅ Tratamento de erros  
✅ Interface interativa  
✅ Exportação de dados  
✅ Documentação completa  
✅ Código limpo e organizado  

---

**Boa sorte com seu trabalho! 🚀**


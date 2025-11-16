# 🗺️ Projeto de Integração com API CEP Aberto

## 📚 Trabalho de Faculdade - Validação e Integração entre APIs

Este projeto demonstra a integração com a API CEP Aberto para buscar e validar CEPs de todo o Brasil, desenvolvido como trabalho acadêmico sobre validação e integração entre APIs REST.

---

## 🎯 Objetivos do Projeto

- ✅ Demonstrar integração com API REST
- ✅ Implementar validação de dados recebidos
- ✅ Tratar erros e exceções adequadamente
- ✅ Manipular múltiplas requisições HTTP
- ✅ Exportar dados em diferentes formatos (JSON e CSV)
- ✅ Criar interface interativa para usuário
- ✅ Documentar código e funcionalidades

---

## 🚀 Funcionalidades

### 1. **Busca de CEP Individual**
- Busca informações completas de um CEP específico
- Validação automática do formato do CEP
- Formatação de dados para exibição

### 2. **Busca de Múltiplos CEPs**
- Busca diversos CEPs em uma única operação
- Controle de intervalo entre requisições
- Barra de progresso e estatísticas

### 3. **Validação de Dados**
- Verifica integridade dos dados recebidos
- Identifica campos obrigatórios ausentes
- Gera relatório de validação

### 4. **Exportação de Resultados**
- Exporta para formato JSON
- Exporta para formato CSV
- Permite análise posterior dos dados

### 5. **Histórico e Estatísticas**
- Mantém histórico de todas as buscas
- Calcula taxa de sucesso
- Exibe estatísticas detalhadas

### 6. **Busca por Região**
- CEPs organizados por região do Brasil
- Busca de capitais brasileiras
- Busca por estado

---

## 📋 Requisitos

### Pré-requisitos
- Python 3.7 ou superior
- Conexão com internet
- Token da API CEP Aberto (gratuito)

### Dependências
```
requests==2.31.0
```

---

## 🔧 Instalação

### 1. Clone ou baixe o projeto

```bash
cd cep_api_integration
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure seu token

Edite o arquivo `config.py` e insira seu token da API:

```python
API_TOKEN = "seu_token_aqui"
```

> 💡 **Como obter um token gratuito:**
> 1. Acesse: https://www.cepaberto.com/
> 2. Crie uma conta gratuita
> 3. Copie seu token de autenticação

---

## 💻 Como Usar

### Método 1: Programa Principal (Interativo)

Execute o arquivo principal para um menu interativo completo:

```bash
python main.py
```

O programa oferece um menu com as seguintes opções:
- Buscar um CEP
- Buscar múltiplos CEPs
- Buscar CEPs de capitais
- Buscar CEPs por região
- Ver histórico de buscas
- Ver estatísticas
- Executar exemplos

### Método 2: Exemplos de Demonstração

Execute o arquivo de exemplos para ver todas as funcionalidades:

```bash
python exemplos.py
```

Inclui 6 exemplos práticos:
1. Busca simples de CEP
2. Busca de múltiplos CEPs
3. Validação de dados
4. Exportação de resultados
5. CEPs por estado
6. Tratamento de erros

### Método 3: Uso Programático

Você também pode usar a classe `CepAbertoAPI` em seus próprios scripts:

```python
from cep_api import CepAbertoAPI

# Inicializa a API
api = CepAbertoAPI(token="seu_token_aqui")

# Busca um CEP
resultado = api.buscar_cep("01001000")

# Exibe informações
if resultado:
    print(f"Logradouro: {resultado['logradouro']}")
    print(f"Cidade: {resultado['cidade']['nome']}")
    print(f"Estado: {resultado['estado']['sigla']}")
```

---

## 📁 Estrutura do Projeto

```
cep_api_integration/
│
├── cep_api.py           # Classe principal de integração com API
├── main.py              # Programa principal com menu interativo
├── exemplos.py          # Exemplos de uso e demonstrações
├── config.py            # Arquivo de configuração
├── requirements.txt     # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo git
└── README.md           # Este arquivo
```

---

## 🔍 Exemplos de Uso

### Exemplo 1: Busca Simples

```python
from cep_api import CepAbertoAPI
from config import API_TOKEN

api = CepAbertoAPI(token=API_TOKEN)
resultado = api.buscar_cep("01001000")

if resultado:
    print(f"📍 {resultado['logradouro']}, {resultado['bairro']}")
    print(f"   {resultado['cidade']['nome']}/{resultado['estado']['sigla']}")
```

### Exemplo 2: Múltiplos CEPs

```python
ceps = ["01001000", "20040020", "30130100"]
resultados = api.buscar_multiplos_ceps(ceps, intervalo=0.5)

print(f"Encontrados: {len(resultados)} CEPs")
```

### Exemplo 3: Validação

```python
resultado = api.buscar_cep("01001000")
validacao = api.validar_dados_cep(resultado)

print(f"Status: {'✅ VÁLIDO' if validacao['valido'] else '❌ INVÁLIDO'}")
print(f"Campos presentes: {validacao['campos_presentes']}")
```

### Exemplo 4: Exportação

```python
resultados = api.buscar_multiplos_ceps(ceps)
api.exportar_resultados(resultados, "meus_ceps.json")
```

### Exemplo 5: Estatísticas

```python
stats = api.obter_estatisticas()
print(f"Total de buscas: {stats['total_buscas']}")
print(f"Taxa de sucesso: {stats['taxa_sucesso']}%")
```

---

## 📊 Formato dos Dados

### Resposta da API

```json
{
  "cep": "01001000",
  "logradouro": "Praça da Sé",
  "complemento": "- lado ímpar",
  "bairro": "Sé",
  "cidade": {
    "nome": "São Paulo",
    "ddd": 11,
    "ibge": "3550308"
  },
  "estado": {
    "sigla": "SP"
  },
  "latitude": "-23.5479099981",
  "longitude": "-46.636",
  "altitude": 760.0
}
```

### Campos Disponíveis

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `cep` | string | Número do CEP (8 dígitos) |
| `logradouro` | string | Nome da rua/avenida |
| `complemento` | string | Informações complementares |
| `bairro` | string | Nome do bairro |
| `cidade.nome` | string | Nome da cidade |
| `cidade.ddd` | int | Código DDD |
| `cidade.ibge` | string | Código IBGE |
| `estado.sigla` | string | Sigla do estado (UF) |
| `latitude` | string | Coordenada de latitude |
| `longitude` | string | Coordenada de longitude |
| `altitude` | float | Altitude em metros |

---

## 🛡️ Tratamento de Erros

O projeto implementa tratamento robusto de erros:

### Tipos de Erros Tratados

1. **CEP Inválido** (formato incorreto)
   - Retorna: `None`
   - Mensagem: "CEP inválido"

2. **CEP Não Encontrado** (404)
   - Retorna: `None`
   - Mensagem: "CEP não encontrado na base de dados"

3. **Erro de Autenticação** (401)
   - Retorna: `None`
   - Mensagem: "Erro de autenticação. Verifique seu token"

4. **Limite de Requisições** (429)
   - Retorna: `None`
   - Mensagem: "Limite de requisições excedido"

5. **Timeout**
   - Retorna: `None`
   - Mensagem: "Timeout ao buscar CEP"

6. **Erro de Conexão**
   - Retorna: `None`
   - Mensagem: "Erro de conexão"

---

## 🎓 Conceitos Aplicados

Este projeto demonstra os seguintes conceitos de programação e integração de APIs:

### 1. **API REST**
- Requisições HTTP GET
- Headers de autenticação
- Parâmetros de URL
- Códigos de status HTTP

### 2. **Validação de Dados**
- Validação de formato (CEP)
- Validação de campos obrigatórios
- Validação de tipos de dados
- Geração de relatórios de validação

### 3. **Tratamento de Erros**
- Try-except para exceções
- Verificação de status codes
- Timeouts e retry logic
- Mensagens de erro amigáveis

### 4. **Boas Práticas**
- Código modular e reutilizável
- Documentação (docstrings)
- Type hints
- Separação de responsabilidades
- Configuração externa

### 5. **Manipulação de Dados**
- JSON parsing
- Exportação CSV
- Estruturas de dados (listas, dicionários)
- Formatação de strings

---

## 📝 Lista de CEPs para Teste

### Capitais Brasileiras

| Cidade | UF | CEP | Localização |
|--------|----|----|-------------|
| São Paulo | SP | 01001-000 | Praça da Sé |
| Rio de Janeiro | RJ | 20040-020 | Centro |
| Belo Horizonte | MG | 30130-100 | Centro |
| Salvador | BA | 40020-000 | Centro |
| Fortaleza | CE | 60010-000 | Centro |
| Brasília | DF | 70040-902 | Esplanada dos Ministérios |
| Curitiba | PR | 80010-000 | Centro |
| Recife | PE | 50010-000 | Recife |
| Porto Alegre | RS | 90010-000 | Centro |
| Manaus | AM | 69005-000 | Centro |

### Regiões do Brasil

**Sudeste:**
- 01001000 (São Paulo/SP)
- 20040020 (Rio de Janeiro/RJ)
- 30130100 (Belo Horizonte/MG)
- 29010000 (Vitória/ES)

**Sul:**
- 80010000 (Curitiba/PR)
- 90010000 (Porto Alegre/RS)
- 88010000 (Florianópolis/SC)

**Nordeste:**
- 40020000 (Salvador/BA)
- 50010000 (Recife/PE)
- 60010000 (Fortaleza/CE)
- 57020000 (Maceió/AL)

**Norte:**
- 69005000 (Manaus/AM)
- 66010000 (Belém/PA)
- 78010000 (Cuiabá/MT)

**Centro-Oeste:**
- 70040902 (Brasília/DF)
- 74003010 (Goiânia/GO)
- 79002000 (Campo Grande/MS)

---

## 🔒 Segurança

### Boas Práticas Implementadas

1. **Token não exposto no código**
   - Usar arquivo `config.py`
   - Adicionar `config.py` ao `.gitignore` em produção

2. **Timeout nas requisições**
   - Evita travamento do programa
   - Limite de 10 segundos por requisição

3. **Intervalo entre requisições**
   - Respeita os limites da API
   - Evita bloqueio por excesso de requisições

4. **Validação de entrada**
   - Verifica formato do CEP antes de enviar
   - Previne requisições desnecessárias

---

## 📚 Documentação da API

### Documentação Oficial
- Site: https://www.cepaberto.com/
- API Docs: https://www.cepaberto.com/api_v3

### Endpoint Utilizado

```
GET https://www.cepaberto.com/api/v3/cep?cep={CEP}
```

### Autenticação

```
Authorization: Token token={SEU_TOKEN}
```

### Limites
- Plano gratuito: até 1000 requisições/dia
- Plano pago: requisições ilimitadas

---

## 🤝 Contribuindo

Este é um projeto acadêmico, mas sugestões são bem-vindas!

### Como contribuir:
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como trabalho de faculdade.

---

## 👨‍💻 Autor

Desenvolvido como trabalho de faculdade sobre **Validação e Integração entre APIs**.

---

## 🙏 Agradecimentos

- **API CEP Aberto** - pela disponibilização gratuita da API
- **Correios** - pelos dados de CEP
- **Python Community** - pelas bibliotecas utilizadas

---

## 📞 Suporte

### Problemas Comuns

**1. Erro de autenticação**
- Verifique se o token está correto no `config.py`
- Confirme que o token está ativo em cepaberto.com

**2. CEP não encontrado**
- Verifique se o CEP existe
- Tente remover a formatação (hífens)

**3. Timeout**
- Verifique sua conexão com internet
- Aumente o tempo de timeout no código

**4. Limite de requisições**
- Aguarde algumas horas
- Considere upgrade para plano pago

---

## 📖 Referências

- [Documentação Python Requests](https://requests.readthedocs.io/)
- [API REST Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [CEP Aberto API](https://www.cepaberto.com/)

---

## 🎯 Conclusão

Este projeto demonstra de forma completa a integração com APIs REST, incluindo:
- ✅ Autenticação com tokens
- ✅ Requisições HTTP
- ✅ Validação de dados
- ✅ Tratamento de erros
- ✅ Exportação de dados
- ✅ Interface interativa
- ✅ Documentação completa

Ideal para apresentação acadêmica sobre integração e validação de APIs! 🚀

---

**Versão:** 1.0.0  
**Data:** Novembro 2024  
**Status:** ✅ Completo


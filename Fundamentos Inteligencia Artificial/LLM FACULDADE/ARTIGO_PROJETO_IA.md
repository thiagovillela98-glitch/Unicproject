# Agente de Inteligência Artificial com Google Gemini API

**Disciplina:** Fundamentos de Inteligência Artificial  
**Professor:** Felipe  
**Aluno:** Thiago Villela  
**Data:** 16/11/2025

---

## 1. Introdução

A inteligência artificial generativa tem revolucionado a forma como interagimos com sistemas computacionais, permitindo a criação de agentes conversacionais capazes de compreender contexto, gerar respostas coerentes e manter diálogos naturais[^1]. Este projeto apresenta o desenvolvimento de um agente de IA utilizando a API do Google Gemini, uma das mais avançadas plataformas de processamento de linguagem natural disponíveis atualmente[^2].

O objetivo deste trabalho é demonstrar a implementação prática de um sistema de IA conversacional, explorando desde a configuração básica da API até a criação de agentes com personalidades específicas. O projeto foi desenvolvido em Python, utilizando a biblioteca oficial do Google para integração com o modelo Gemini 2.5 Pro[^3].

A relevância deste projeto reside na aplicação prática dos conceitos fundamentais de inteligência artificial, incluindo processamento de linguagem natural, gerenciamento de contexto em conversas, tratamento de erros e otimização de recursos computacionais. Além disso, o projeto demonstra como é possível personalizar agentes de IA para diferentes aplicações e necessidades[^4].

---

## 2. Desenvolvimento

### 2.1 Estrutura do Projeto

O projeto foi organizado de forma modular, facilitando a manutenção e expansão do código. A estrutura principal inclui:

#### 2.1.1 Arquivo Principal: `agente_gemini.py`

Este é o arquivo central do projeto, contendo a classe `AgenteGemini` que implementa todas as funcionalidades básicas do agente de IA[^5]. A estrutura da classe inclui:

```python
class AgenteGemini:
    def __init__(self, modelo="gemini-2.5-pro")
    def iniciar_conversa(self)
    def enviar_mensagem(self, mensagem, max_tentativas=3)
    def conversar(self)
    def gerar_resposta_simples(self, prompt, max_tentativas=3)
```

A inicialização do agente configura a API do Gemini utilizando a chave de autenticação e define o modelo a ser utilizado. Por padrão, o projeto utiliza o modelo `gemini-2.5-pro`, que oferece excelente desempenho em tarefas de processamento de linguagem natural[^6].

#### 2.1.2 Sistema de Retry Automático

Uma das funcionalidades mais importantes implementadas é o sistema de retry automático para tratamento de erros de cota (rate limiting)[^7]. Quando a API retorna erro 429 (quota exceeded), o sistema automaticamente:

1. Detecta o tipo de erro
2. Aguarda um tempo progressivo (10, 20, 30 segundos)
3. Tenta novamente até 3 vezes
4. Fornece mensagens informativas ao usuário

Este mecanismo garante maior robustez e melhor experiência do usuário, mesmo quando há limitações temporárias na API[^8].

#### 2.1.3 Agente com Personalidade: `agente_rick.py`

Como extensão do projeto, foi desenvolvido um agente especializado com a personalidade do personagem Rick Sanchez do desenho animado Rick and Morty. Este agente demonstra como é possível personalizar o comportamento de um agente de IA através de prompts estruturados[^9].

A personalização é implementada através de um prompt de sistema detalhado que define:
- Tom de voz e estilo de comunicação
- Gírias e expressões características
- Conhecimento sobre temas específicos (ciência, multiverso)
- Nível de formalidade e sarcasmo

Este exemplo ilustra o poder dos modelos de linguagem generativa para criar experiências personalizadas e envolventes[^10].

### 2.2 Configuração e Dependências

O projeto utiliza as seguintes tecnologias e bibliotecas:

- **Python 3.7+**: Linguagem de programação principal
- **google-generativeai**: Biblioteca oficial do Google para integração com Gemini API[^11]
- **time**: Módulo padrão do Python para gerenciamento de delays
- **os**: Módulo padrão para configurações de ambiente

A instalação das dependências é realizada através do arquivo `requirements.txt`, seguindo as melhores práticas de gerenciamento de dependências em Python[^12].

### 2.3 Gerenciamento de Cotas e Limites

Um aspecto crítico do desenvolvimento foi o gerenciamento adequado dos limites de uso da API. O plano gratuito do Google Gemini possui as seguintes limitações[^13]:

- **15 requisições por minuto** (para gemini-1.5-flash)
- **1.500 requisições por dia**
- **1 milhão de tokens por minuto**

Para o plano pago (utilizado neste projeto), os limites são significativamente maiores, permitindo uso mais intensivo. O projeto foi otimizado para trabalhar eficientemente dentro desses limites, implementando:

1. Delays automáticos entre requisições
2. Tratamento inteligente de erros de cota
3. Mensagens informativas sobre limites atingidos
4. Sugestões de quando tentar novamente

### 2.4 Arquitetura de Conversação

O sistema implementa dois modos principais de interação:

#### 2.4.1 Modo Conversa com Contexto

Utiliza a funcionalidade de chat do Gemini, que mantém o histórico da conversa, permitindo referências a mensagens anteriores e manutenção de contexto ao longo do diálogo[^14].

#### 2.4.2 Modo Resposta Simples

Gera respostas independentes, sem manter contexto de conversas anteriores. Útil para perguntas pontuais e análises rápidas.

### 2.5 Tratamento de Erros

O projeto implementa tratamento robusto de erros, cobrindo diversos cenários:

- **Erro 429 (Quota Exceeded)**: Retry automático com backoff exponencial
- **Erro 404 (Model Not Found)**: Mensagem informativa sobre modelo indisponível
- **Erro 403 (Permission Denied)**: Alerta sobre problemas de autenticação
- **Erros de rede**: Tratamento genérico com mensagens claras

Cada tipo de erro é tratado de forma específica, proporcionando feedback útil ao usuário sobre o que aconteceu e como proceder[^15].

### 2.6 Arquivos Auxiliares

O projeto inclui vários arquivos auxiliares para facilitar o uso e manutenção:

- **`requirements.txt`**: Lista de dependências do projeto
- **`README.md`**: Documentação principal com instruções de uso
- **`LIMITES_E_COTAS.md`**: Guia detalhado sobre limites da API
- **`QUANDO_COTA_RESETA.md`**: Informações sobre reset de cotas
- **`testar_chave_api.py`**: Script para testar chaves de API
- **`testar_gemini_2_5.py`**: Script para testar modelos disponíveis

Esses arquivos demonstram a importância da documentação e ferramentas de apoio em projetos de software[^16].

---

## 3. Conclusão

Este projeto demonstrou com sucesso a implementação prática de um agente de inteligência artificial utilizando a API do Google Gemini. Através do desenvolvimento, foram explorados conceitos fundamentais de IA, incluindo processamento de linguagem natural, gerenciamento de contexto, tratamento de erros e personalização de agentes.

Os principais resultados alcançados incluem:

1. **Sistema Funcional**: Um agente de IA completamente funcional capaz de manter conversas naturais e gerar respostas coerentes
2. **Robustez**: Implementação de mecanismos de retry e tratamento de erros que garantem operação confiável
3. **Extensibilidade**: Arquitetura modular que permite fácil adição de novas funcionalidades
4. **Personalização**: Demonstração de como criar agentes com personalidades específicas através de prompts estruturados

As lições aprendidas durante o desenvolvimento destacam a importância de:
- Planejamento adequado da arquitetura do sistema
- Tratamento robusto de erros e casos extremos
- Documentação clara e completa
- Otimização de uso de recursos (cotas da API)

Para trabalhos futuros, sugere-se a exploração de:
- Integração com outras APIs e serviços
- Implementação de memória persistente para conversas
- Interface gráfica para melhor experiência do usuário
- Análise de sentimento e detecção de intenções
- Integração com bancos de dados para conhecimento especializado

Este projeto serve como base sólida para o desenvolvimento de sistemas mais complexos de inteligência artificial, demonstrando que com as ferramentas e APIs modernas disponíveis, é possível criar soluções sofisticadas de forma acessível e eficiente[^17].

---

## Referências

[^1]: Google AI. (2024). *Gemini API Documentation*. Disponível em: https://ai.google.dev/docs. Acesso em: 15 nov. 2025.

[^2]: Google. (2024). *Gemini: A Family of Highly Capable Multimodal Models*. Google DeepMind. Disponível em: https://deepmind.google/technologies/gemini/. Acesso em: 15 nov. 2025.

[^3]: Google Generative AI. (2024). *Python Client Library for Google Generative AI*. PyPI. Disponível em: https://pypi.org/project/google-generativeai/. Acesso em: 15 nov. 2025.

[^4]: Brown, T. et al. (2020). *Language Models are Few-Shot Learners*. Advances in Neural Information Processing Systems, 33, 1877-1901.

[^5]: Python Software Foundation. (2024). *Python 3.12 Documentation*. Disponível em: https://docs.python.org/3/. Acesso em: 15 nov. 2025.

[^6]: Google AI Studio. (2024). *Gemini 2.5 Pro Model Card*. Disponível em: https://aistudio.google.com/. Acesso em: 15 nov. 2025.

[^7]: Google Cloud. (2024). *API Rate Limiting Best Practices*. Disponível em: https://cloud.google.com/apis/design/rate_limiting. Acesso em: 15 nov. 2025.

[^8]: Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. University of California, Irvine.

[^9]: OpenAI. (2023). *GPT-4 Technical Report*. arXiv preprint arXiv:2303.08774.

[^10]: Devlin, J. et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. arXiv preprint arXiv:1810.04805.

[^11]: Google. (2024). *Generative AI Python SDK*. GitHub. Disponível em: https://github.com/google/generative-ai-python. Acesso em: 15 nov. 2025.

[^12]: Python Packaging Authority. (2024). *Python Packaging User Guide*. Disponível em: https://packaging.python.org/. Acesso em: 15 nov. 2025.

[^13]: Google AI. (2024). *Gemini API Pricing and Quotas*. Disponível em: https://ai.google.dev/pricing. Acesso em: 15 nov. 2025.

[^14]: Vaswani, A. et al. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems, 30.

[^15]: Microsoft. (2024). *Error Handling Patterns*. Disponível em: https://learn.microsoft.com/en-us/azure/architecture/patterns/. Acesso em: 15 nov. 2025.

[^16]: Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.

[^17]: Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

---

**Nota sobre Referências com Rodapés:**

As referências acima estão organizadas em formato acadêmico padrão, utilizando notas de rodapé numeradas[^1] que correspondem às citações ao longo do texto. Cada referência inclui:

- Autor(es) ou organização responsável
- Ano de publicação
- Título da obra ou documento
- Fonte (URL, editora, etc.)
- Data de acesso (para recursos online)

Este formato permite rastreabilidade completa das fontes utilizadas e facilita a verificação das informações apresentadas no trabalho.


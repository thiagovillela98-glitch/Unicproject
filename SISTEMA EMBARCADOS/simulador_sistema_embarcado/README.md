# 🖥️ Simulador de Sistema Embarcado - Monitoramento de Temperatura

## 📋 Descrição

Este é um **simulador completo** de um sistema embarcado de monitoramento de temperatura e umidade, desenvolvido em Python com interface gráfica. 

**Não requer nenhum componente físico!** Tudo é simulado virtualmente.

O sistema replica o comportamento de um Arduino com sensores DHT11, display LCD, LEDs indicadores e sistema de alarme, demonstrando todos os conceitos de integração hardware-software de forma visual e interativa.

---

## ✨ Características

### 🎯 Funcionalidades Principais

- ✅ **Simulação realista** de sensor DHT11 (com ruído e variações)
- ✅ **Display LCD virtual** 16x2 (igual ao físico)
- ✅ **3 LEDs indicadores** com cores dinâmicas (Verde, Amarelo, Vermelho)
- ✅ **Sistema de alertas** multinível automático
- ✅ **Alarme sonoro** (beep do sistema) quando crítico
- ✅ **Gráficos em tempo real** de temperatura e umidade
- ✅ **Log de eventos** com timestamp
- ✅ **Controles interativos** para simular condições
- ✅ **Modo automático** com variações realistas
- ✅ **Estatísticas** (média, máxima, mínima)

### 🎨 Interface Gráfica

- **Design moderno** e profissional
- **Dashboard completo** com múltiplos painéis
- **Visualização em tempo real** de todos os dados
- **Cores temáticas** (dark mode)
- **Responsivo** e redimensionável

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.7 ou superior** instalado
- Bibliotecas usadas: **todas nativas do Python!** (tkinter, threading, random, datetime)

### Instalação

1. **Verifique se tem Python instalado:**

```bash
python --version
```

ou

```bash
python3 --version
```

2. **Não precisa instalar nada!** Todas as bibliotecas já vêm com Python.

### Executando

**Opção 1: Pelo Terminal/CMD**

```bash
cd simulador_sistema_embarcado
python main.py
```

ou

```bash
python3 main.py
```

**Opção 2: No Visual Studio Code**

1. Abra a pasta `simulador_sistema_embarcado` no VS Code
2. Abra o arquivo `main.py`
3. Pressione **F5** ou clique em "Run" → "Run Without Debugging"
4. Ou clique com botão direito no arquivo e selecione "Run Python File in Terminal"

**Opção 3: Duplo clique** (Windows)

- Basta dar duplo clique no arquivo `main.py` (se Python estiver configurado)

---

## 🎮 Como Usar o Simulador

### Interface Principal

A janela do simulador é dividida em 3 colunas:

#### 📟 Coluna Esquerda: Display e Indicadores
- **Display LCD 16x2:** Mostra temperatura e umidade em tempo real
- **LEDs Indicadores:** 
  - 🟢 Verde: Temperatura normal (< 25°C)
  - 🟡 Amarelo: Temperatura elevada (25-30°C)  
  - 🔴 Vermelho: Temperatura crítica (> 30°C)
- **Status do Sistema:** Exibe estado atual e alarme

#### 📊 Coluna Central: Gráficos
- **Gráfico de Temperatura:** Linha do tempo com últimas 50 leituras
- **Gráfico de Umidade:** Histórico visual da umidade

#### 🎮 Coluna Direita: Controles e Log
- **Controles de Simulação:**
  - 🔥 **Aquecer:** Aumenta temperatura em +5°C
  - ❄️ **Resfriar:** Diminui temperatura em -5°C
  - 🔄 **Resetar:** Volta às condições normais
  - 🤖 **Modo Automático:** Simula variações naturais
- **Estatísticas:** Média, máxima e mínima
- **Log de Eventos:** Registro de todas as ações

### Testando o Sistema

1. **Inicie o programa** - O sistema começa em temperatura normal
2. **Observe o LCD** - Valores atualizando a cada 2 segundos
3. **Teste o aquecimento:**
   - Clique em "🔥 Aquecer" algumas vezes
   - Observe o LED mudando de Verde → Amarelo → Vermelho
   - Quando > 30°C, o alarme é acionado (beep + status vermelho)
4. **Veja os gráficos** - Linhas sendo desenhadas em tempo real
5. **Confira o log** - Todos os eventos sendo registrados
6. **Tente o modo automático** - Ative para variações realistas

---

## 📚 Conceitos Demonstrados

Este simulador demonstra os seguintes conceitos de sistemas embarcados:

### Hardware (Simulado)
- ✅ Leitura de sensores digitais (DHT11)
- ✅ Controle de display LCD (16x2)
- ✅ Controle de LEDs indicadores
- ✅ Acionamento de alarme (buzzer)
- ✅ Interface de I/O digital

### Software
- ✅ Loop principal de leitura (main loop)
- ✅ Temporização (leituras a cada 2s)
- ✅ Lógica de decisão (alertas multinível)
- ✅ Multithreading (leitura em thread separada)
- ✅ Interface homem-máquina (HMI)
- ✅ Logging de eventos
- ✅ Tratamento de dados (média, máx, mín)

### Integração
- ✅ Hardware + Software trabalhando juntos
- ✅ Processamento em tempo real
- ✅ Sistema de eventos e respostas
- ✅ Visualização de dados
- ✅ Controle e monitoramento

---

## 🎓 Para Apresentação

### Roteiro Sugerido (5-7 minutos)

**1. Introdução (1 min)**
- "Desenvolvi um simulador de sistema embarcado que replica um Arduino real"
- "Não precisei de componentes físicos - tudo é simulado"

**2. Demonstração Visual (2 min)**
- Mostre a interface completa
- Explique cada seção (LCD, LEDs, gráficos)

**3. Teste em Tempo Real (3 min)**
- Execute o programa ao vivo
- Aqueça o sistema e mostre as transições
- Demonstre o alarme acionando
- Mostre os gráficos sendo desenhados
- Ative modo automático

**4. Código e Conceitos (1 min)**
- Mostre rapidamente o código no VS Code
- Explique a arquitetura (classes, threading)
- Mencione conceitos de sistemas embarcados

**5. Conclusão (30 seg)**
- Vantagens de usar simulador
- Aplicações práticas
- Facilidade de teste e desenvolvimento

---

## 💻 Estrutura do Código

### Classe `SensorSimulator`
Simula o comportamento do sensor DHT11:
- Temperatura base + variações + ruído
- Métodos: `ler_temperatura()`, `ler_umidade()`, `aquecer()`, `resfriar()`

### Classe `SistemaMonitoramento`
Sistema principal com GUI:
- Gerencia interface gráfica (tkinter)
- Loop de leitura em thread separada
- Atualização de LEDs, LCD, gráficos
- Sistema de alertas e logs

### Função `main()`
Ponto de entrada do programa

---

## 🎨 Personalização

### Ajustar Limiares de Temperatura

No arquivo `main.py`, altere:

```python
self.TEMP_NORMAL = 25.0   # Altere para o valor desejado
self.TEMP_ELEVADA = 30.0  # Altere para o valor desejado
```

### Modificar Cores

Edite as variáveis de cor na classe:

```python
self.COR_VERDE = "#00ff00"
self.COR_AMARELO = "#ffff00"
self.COR_VERMELHO = "#ff0000"
```

### Alterar Intervalo de Leitura

Na função `loop_leitura()`:

```python
time.sleep(2)  # Altere para o intervalo desejado (segundos)
```

---

## 🐛 Solução de Problemas

### Erro "tkinter not found"

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:** tkinter já vem com Python

### Janela não abre

- Verifique se está executando Python 3.7+
- Tente executar pelo terminal para ver erros
- Certifique-se de que não há outro processo usando a interface gráfica

### Gráficos não aparecem

- Redimensione a janela
- Os gráficos aparecem após ~10 segundos (10 leituras)

---

## 📊 Comparação: Simulador vs Hardware Real

| Aspecto | Hardware Real | Simulador |
|---------|--------------|-----------|
| **Custo** | R$ 90-150 | R$ 0 (grátis!) |
| **Tempo de montagem** | 45-60 min | 2 minutos |
| **Componentes** | Arduino, sensores, LEDs, etc. | Apenas Python |
| **Testes** | Limitado por hardware | Ilimitado |
| **Portabilidade** | Precisa levar tudo | Apenas código |
| **Depuração** | Difícil | Fácil (logs, prints) |
| **Visualização** | Display pequeno | Dashboard completo |
| **Gráficos** | Requer código extra | Já incluído |
| **Aprendizado** | Conceitos de HW/SW | Conceitos de SW + Lógica |

---

## 🌟 Vantagens do Simulador

### Para Desenvolvimento
- ✅ Teste rápido de lógica e algoritmos
- ✅ Debug mais fácil
- ✅ Sem risco de queimar componentes
- ✅ Pode testar condições extremas

### Para Apresentação
- ✅ Não depende de hardware funcionando
- ✅ Visual mais impressionante
- ✅ Fácil de replicar/demonstrar
- ✅ Pode rodar em qualquer computador

### Para Aprendizado
- ✅ Foco nos conceitos, não na montagem
- ✅ Experimentação livre
- ✅ Visualização melhor dos dados
- ✅ Curva de aprendizado suave

---

## 🚀 Expansões Possíveis

### Nível Básico
- [ ] Adicionar mais tipos de sensores
- [ ] Salvar dados em arquivo CSV
- [ ] Modo noturno/diurno

### Nível Intermediário
- [ ] Exportar gráficos como imagem
- [ ] Configurações salvas em JSON
- [ ] Múltiplos perfis de simulação
- [ ] Alarmes configuráveis

### Nível Avançado
- [ ] Interface web (Flask/Django)
- [ ] Banco de dados para histórico
- [ ] Machine Learning para predição
- [ ] API REST para integração
- [ ] Dashboard online

---

## 📞 Suporte

### Recursos
- **Python Docs:** https://docs.python.org/3/
- **Tkinter Tutorial:** https://docs.python.org/3/library/tkinter.html
- **Sistemas Embarcados:** https://www.embedded.com/

### Comunidades
- Stack Overflow
- Reddit r/Python
- Python Brasil (Telegram/Discord)

---

## ✅ Checklist de Entrega

- [x] Código completo e funcional
- [x] Interface gráfica profissional
- [x] Documentação detalhada
- [x] Fácil de executar (zero instalação)
- [x] Demonstra conceitos de sistemas embarcados
- [x] Visual impressionante
- [x] Pronto para apresentação

---

## 🏆 Diferenciais

✨ **Sistema completo sem gastar nada**  
✨ **Interface gráfica profissional**  
✨ **Gráficos em tempo real**  
✨ **Código bem estruturado (OOP)**  
✨ **Fácil de usar e demonstrar**  
✨ **Conceitos reais de sistemas embarcados**  
✨ **Impressiona visualmente**  

---

## 👨‍💻 Desenvolvimento

**Projeto:** Sistema Embarcado de Monitoramento  
**Linguagem:** Python 3  
**Interface:** Tkinter  
**Paradigma:** Orientação a Objetos  
**Data:** Novembro 2025  

---

## 📝 Licença

Projeto educacional de código aberto.  
Livre para uso e modificação.

---

## 🎉 Conclusão

Este simulador oferece uma forma **prática, visual e gratuita** de demonstrar conceitos de sistemas embarcados, sem necessidade de componentes físicos.

Ideal para apresentações, aprendizado e desenvolvimento de lógica de controle antes de implementar em hardware real.

**Execute agora e impressione-se com o resultado!** 🚀

---

**Comando rápido para executar:**

```bash
python main.py
```

**Pronto! Só isso! ✨**


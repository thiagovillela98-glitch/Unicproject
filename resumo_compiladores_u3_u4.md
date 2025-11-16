# Resumo - Unidades 3 e 4: Compiladores

**Nome do Aluno:** Thiago Villela Saturnino Da Silva  
**Nome do Professor:** Felipe  
**Nome da Faculdade:** Universidade Unic Beira Rio  
**Data:** 16/11/2025

---

## Introdução

Os compiladores são programas fundamentais na computação, responsáveis por traduzir código-fonte de linguagens de alto nível para código de máquina executável. Este resumo aborda conceitos essenciais apresentados nas Unidades 3 e 4 da disciplina de Compiladores, explorando desde estruturas de dados utilizadas na compilação até a geração final de código. A Unidade 3 concentra-se em aspectos da análise e organização de informações durante a compilação, enquanto a Unidade 4 foca na geração e otimização do código resultante, culminando com a proposta de linguagens inovadoras.

## Desenvolvimento

### Unidade 3 - Análise e Estruturas de Compilação

**Tabela de Símbolos**

A tabela de símbolos é uma estrutura de dados crucial no processo de compilação, funcionando como um repositório centralizado de informações sobre identificadores presentes no código-fonte. Ela armazena dados sobre variáveis, funções, constantes e tipos, incluindo atributos como nome, tipo, escopo, endereço de memória e outras propriedades relevantes. Durante a compilação, a tabela de símbolos é consultada e atualizada constantemente pelas diferentes fases do compilador, permitindo verificação de tipos, detecção de erros semânticos e geração de código eficiente. Sua implementação pode utilizar diversas estruturas, como tabelas hash ou árvores, priorizando eficiência nas operações de inserção, busca e atualização.

**Tradução Dirigida pela Sintaxe**

A tradução dirigida pela sintaxe é uma técnica que combina análise sintática com ações semânticas, permitindo que o compilador não apenas reconheça a estrutura do programa, mas também execute operações durante o processo de análise. Utiliza gramáticas atribuídas, onde cada produção da gramática possui atributos e regras semânticas associadas. Existem dois tipos principais de atributos: sintetizados (calculados a partir dos filhos na árvore sintática) e herdados (passados de nós pais ou irmãos). Esta abordagem é fundamental para construir representações intermediárias, calcular expressões, verificar tipos e gerar código durante a análise sintática, tornando o processo de compilação mais integrado e eficiente.

**Análise Sintática Top-Down**

A análise sintática top-down é uma estratégia que constrói a árvore de derivação a partir da raiz (símbolo inicial da gramática) em direção às folhas (tokens do programa). Os principais métodos incluem análise recursiva descendente e análise preditiva (LL). Na análise recursiva descendente, cada não-terminal da gramática é implementado como uma função recursiva que tenta reconhecer sua produção correspondente. Já os analisadores preditivos LL(1) utilizam uma tabela de análise construída a partir dos conjuntos FIRST e FOLLOW, permitindo determinar qual produção aplicar baseando-se apenas no próximo token. Esta técnica é intuitiva, facilita a implementação manual de compiladores e permite mensagens de erro mais claras, porém apresenta limitações com gramáticas que possuem recursão à esquerda ou ambiguidade.

### Unidade 4 - Geração e Otimização de Código

**Geração de Código Intermediário**

A geração de código intermediário é uma fase essencial que produz uma representação abstrata do programa, independente da arquitetura alvo. As formas mais comuns incluem código de três endereços, onde cada instrução possui no máximo um operador e três operandos, árvores sintáticas abstratas (AST) que representam a estrutura hierárquica do programa, e notação pós-fixada. O código intermediário facilita a otimização, pois permite aplicar transformações independentes de plataforma, além de tornar o compilador mais portável, já que apenas o back-end precisa ser reescrito para diferentes arquiteturas. Esta representação intermediária serve como ponte entre a análise semântica e a geração de código de máquina.

**Geração de Código e Otimização**

A geração de código final transforma a representação intermediária em código de máquina ou assembly específico para a arquitetura alvo. Este processo envolve seleção de instruções adequadas, alocação de registradores e ordenação de instruções para maximizar desempenho. A otimização de código pode ocorrer em diversos níveis: local (dentro de blocos básicos), global (em toda a função) e interprocedimental. Técnicas comuns incluem eliminação de subexpressões comuns, propagação de constantes, eliminação de código morto, movimentação de código invariante em laços e desenrolamento de loops. O objetivo é produzir código eficiente em termos de tempo de execução e uso de memória, mantendo a semântica original do programa.

**Especificação de Linguagem Inovadora**

A especificação de uma proposta de linguagem inovadora envolve definir sintaxe, semântica e características distintivas que atendam necessidades específicas de programação. Este processo inclui a definição formal da gramática, sistema de tipos, modelo de execução, paradigma de programação (imperativo, funcional, orientado a objetos, etc.) e recursos especiais. Uma linguagem inovadora pode focar em aspectos como segurança de memória, concorrência simplificada, expressividade sintática ou domínios específicos. A especificação deve considerar também aspectos de implementação, como a viabilidade de construir um compilador ou interpretador eficiente, além de documentar claramente as regras e convenções da linguagem para garantir sua usabilidade e adoção.

## Conclusão

As Unidades 3 e 4 apresentam conceitos fundamentais que compõem a espinha dorsal do desenvolvimento de compiladores modernos. A compreensão de estruturas como tabelas de símbolos, técnicas de análise sintática e tradução dirigida pela sintaxe fornece a base necessária para processar e compreender programas escritos em linguagens de alto nível. Por outro lado, o domínio das técnicas de geração de código intermediário e otimização possibilita a criação de código executável eficiente. A capacidade de especificar novas linguagens representa a culminação desse conhecimento, permitindo aos desenvolvedores criar ferramentas de programação adaptadas a necessidades específicas. Estes conceitos são essenciais não apenas para quem deseja construir compiladores, mas para qualquer profissional de computação que busca compreender profundamente como o código é transformado desde sua escrita até sua execução no hardware.

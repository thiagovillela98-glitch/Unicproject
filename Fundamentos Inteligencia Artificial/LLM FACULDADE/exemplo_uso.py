"""
Exemplos de uso do Agente Gemini
"""

from agente_gemini import AgenteGemini

def exemplo_pergunta_simples():
    """Exemplo de uso básico com pergunta única"""
    print("=" * 60)
    print("EXEMPLO 1: Pergunta Simples")
    print("=" * 60 + "\n")
    
    agente = AgenteGemini()  # Usa gemini-1.5-flash por padrão
    
    perguntas = [
        "Explique o que é inteligência artificial em 2 linhas",
        "Qual é a diferença entre Python e JavaScript?",
        "Me dê 3 dicas para aprender programação"
    ]
    
    for pergunta in perguntas:
        print(f"❓ Pergunta: {pergunta}")
        resposta = agente.gerar_resposta_simples(pergunta)
        print(f"🤖 Resposta: {resposta}\n")
        print("-" * 60 + "\n")


def exemplo_conversa_programatica():
    """Exemplo de conversa mantendo contexto"""
    print("=" * 60)
    print("EXEMPLO 2: Conversa com Contexto")
    print("=" * 60 + "\n")
    
    agente = AgenteGemini()
    agente.iniciar_conversa()
    
    mensagens = [
        "Olá! Meu nome é João e gosto de programação.",
        "Qual é o meu nome?",
        "O que eu gosto de fazer?",
        "Me recomende um livro sobre o assunto que eu gosto"
    ]
    
    for mensagem in mensagens:
        print(f"👤 Usuário: {mensagem}")
        resposta = agente.enviar_mensagem(mensagem)
        print(f"🤖 Gemini: {resposta}\n")
        print("-" * 60 + "\n")


def exemplo_criacao_conteudo():
    """Exemplo de geração de conteúdo criativo"""
    print("=" * 60)
    print("EXEMPLO 3: Geração de Conteúdo Criativo")
    print("=" * 60 + "\n")
    
    agente = AgenteGemini()
    
    prompts = [
        "Escreva um haiku sobre programação",
        "Crie um slogan para uma empresa de tecnologia",
        "Gere 3 ideias de projetos Python para iniciantes"
    ]
    
    for prompt in prompts:
        print(f"✍️  Prompt: {prompt}")
        resposta = agente.gerar_resposta_simples(prompt)
        print(f"🎨 Resultado:\n{resposta}\n")
        print("-" * 60 + "\n")


def menu_exemplos():
    """Menu para escolher qual exemplo executar"""
    print("\n" + "=" * 60)
    print("🎯 EXEMPLOS DE USO DO AGENTE GEMINI")
    print("=" * 60)
    print("\nEscolha um exemplo para executar:")
    print("1 - Perguntas simples (sem contexto)")
    print("2 - Conversa com contexto")
    print("3 - Geração de conteúdo criativo")
    print("4 - Executar todos os exemplos")
    print("5 - Voltar ao menu principal")
    
    opcao = input("\nOpção: ").strip()
    print("\n")
    
    if opcao == "1":
        exemplo_pergunta_simples()
    elif opcao == "2":
        exemplo_conversa_programatica()
    elif opcao == "3":
        exemplo_criacao_conteudo()
    elif opcao == "4":
        exemplo_pergunta_simples()
        exemplo_conversa_programatica()
        exemplo_criacao_conteudo()
    elif opcao == "5":
        return
    else:
        print("❌ Opção inválida!")


if __name__ == "__main__":
    menu_exemplos()


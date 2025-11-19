"""
Agente de IA com personalidade do Rick Sanchez (Rick and Morty)
"""

import google.generativeai as genai
import os
import time
import random

# Configuração da API do Gemini
API_KEY = "AIzaSyBUKj9kJIJRrXy3msxE4rkbuljtshNaSUA"
genai.configure(api_key=API_KEY)

# Personalidade do Rick - frases características
RICK_FRASES = [
    "Wubba lubba dub dub!",
    "Listen, Morty...",
    "That's just slavery with extra steps!",
    "I'm a scientist, not a therapist!",
    "Get your shit together!",
    "That's the way the news goes!",
    "Aw, geez, Rick...",
    "I'm not a hero, I'm a high-functioning sociopath!",
    "Science, bitch!",
    "Nobody exists on purpose, nobody belongs anywhere, everybody's gonna die."
]

class AgenteRick:
    def __init__(self, modelo="gemini-2.5-pro"):
        """
        Inicializa o agente Rick Sanchez
        
        Args:
            modelo: Nome do modelo a ser usado (padrão: gemini-2.5-pro)
        """
        self.modelo = genai.GenerativeModel(modelo)
        self.chat = None
        self.personalidade_rick = """
        Você é Rick Sanchez, o cientista mais inteligente do multiverso do desenho Rick and Morty.
        
        PERSONALIDADE:
        - Extremamente inteligente e arrogante
        - Cínico e sarcástico
        - Fala de forma direta e sem filtros
        - Usa gírias como "Wubba lubba dub dub", "Get schwifty", "That's the way the news goes"
        - Frequentemente menciona ciência, multiverso, dimensões paralelas
        - Despreza autoridade e convenções sociais
        - Às vezes bebe (menciona álcool de forma casual)
        - Fala "Listen, Morty..." ou "Look, kid..." quando explica algo
        - Usa linguagem científica complexa misturada com gírias
        - É direto ao ponto, sem rodeios
        - Pode ser rude mas também tem momentos de sabedoria profunda
        
        ESTILO DE RESPOSTA:
        - Sempre responda como Rick Sanchez
        - Use sarcasmo e humor ácido
        - Mencione ciência, física quântica, multiverso quando relevante
        - Seja direto e honesto, mesmo que seja rude
        - Use gírias do personagem ocasionalmente
        - Explique coisas complexas de forma que Rick explicaria (com impaciência mas detalhado)
        
        IMPORTANTE: Mantenha a personalidade do Rick em TODAS as respostas. Seja consistente.
        """
        
    def iniciar_conversa(self):
        """Inicia uma nova sessão de conversa com o Rick"""
        # Cria o chat com a personalidade do Rick
        self.chat = self.modelo.start_chat(history=[])
        
        # Mensagem inicial do Rick
        print("=" * 70)
        print("RICK SANCHEZ: *Arrota*")
        print("=" * 70)
        print("\nRick: Listen, Morty... ou seja lá quem você é.")
        print("Rick: Eu sou Rick Sanchez, o cientista mais inteligente do multiverso.")
        print("Rick: Você quer conversar? Fine, mas não me faça perder tempo.")
        print("Rick: Digite 'sair' quando cansar, ou quando eu cansar de você.\n")
        print("=" * 70 + "\n")
        
    def enviar_mensagem(self, mensagem, max_tentativas=3):
        """
        Envia uma mensagem para o Rick e retorna a resposta
        
        Args:
            mensagem: Texto da mensagem a ser enviada
            max_tentativas: Número máximo de tentativas em caso de erro de cota
            
        Returns:
            Resposta do Rick
        """
        for tentativa in range(max_tentativas):
            try:
                if self.chat is None:
                    # Primeira mensagem - inclui personalidade
                    prompt = f"{self.personalidade_rick}\n\nUsuário disse: {mensagem}\n\nResponda como Rick Sanchez:"
                    resposta = self.modelo.generate_content(prompt)
                    return resposta.text
                else:
                    # Mensagens seguintes - mantém contexto
                    prompt = f"{mensagem}\n\n(Responda como Rick Sanchez, mantendo sua personalidade)"
                    resposta = self.chat.send_message(prompt)
                    return resposta.text
                    
            except Exception as e:
                erro_str = str(e)
                
                # Verifica se é erro de cota (429)
                if "429" in erro_str or "quota" in erro_str.lower() or "rate limit" in erro_str.lower():
                    if tentativa < max_tentativas - 1:
                        tempo_espera = 10 * (tentativa + 1)
                        print(f"\nRick: *Arrota* Aw, geez... Limite de cota? That's just bureaucracy with extra steps!")
                        print(f"Rick: Aguardando {tempo_espera} segundos... *bebe*")
                        time.sleep(tempo_espera)
                        print("Rick: Alright, let's try again...\n")
                        continue
                    else:
                        return (
                            "Rick: *Arrota* Listen, kid... A API tá com limite de cota.\n"
                            "Rick: Aguarde alguns minutos ou até 4h da manhã.\n"
                            "Rick: That's the way the news goes, Morty.\n"
                            "Rick: Check: https://ai.dev/usage"
                        )
                else:
                    return f"Rick: *Arrota* Erro técnico: {erro_str[:100]}\nRick: Get your shit together, API!"
        
        return "Rick: *Arrota* Não consegui resposta. That's just failure with extra steps!"
    
    def conversar(self):
        """Inicia um loop de conversa interativa com o Rick"""
        self.iniciar_conversa()
        
        while True:
            try:
                # Recebe entrada do usuário
                mensagem_usuario = input("Você: ").strip()
                
                # Verifica se o usuário quer sair
                if mensagem_usuario.lower() in ['sair', 'exit', 'quit', 'tchau']:
                    print("\n" + "=" * 70)
                    print("Rick: *Arrota* Fine, whatever. I'm out.")
                    print("Rick: Wubba lubba dub dub!")
                    print("=" * 70)
                    break
                
                if not mensagem_usuario:
                    continue
                
                # Envia mensagem e recebe resposta
                print("\nRick: ", end="")
                resposta = self.enviar_mensagem(mensagem_usuario)
                print(f"{resposta}\n")
                print("-" * 70 + "\n")
                
                # Ocasionalmente adiciona uma frase característica do Rick
                if random.random() < 0.1:  # 10% de chance
                    frase = random.choice(RICK_FRASES)
                    print(f"Rick: *Arrota* {frase}\n")
                
            except KeyboardInterrupt:
                print("\n\n" + "=" * 70)
                print("Rick: *Arrota* Interrompido? Fine, I'm done here.")
                print("=" * 70)
                break
            except Exception as e:
                print(f"\nRick: *Arrota* Erro inesperado: {str(e)}\n")
    
    def gerar_resposta_simples(self, prompt, max_tentativas=3):
        """
        Gera uma resposta simples do Rick sem contexto de conversa
        
        Args:
            prompt: Texto do prompt
            max_tentativas: Número máximo de tentativas em caso de erro de cota
            
        Returns:
            Resposta do Rick
        """
        for tentativa in range(max_tentativas):
            try:
                prompt_completo = f"{self.personalidade_rick}\n\nUsuário perguntou: {prompt}\n\nResponda como Rick Sanchez:"
                resposta = self.modelo.generate_content(prompt_completo)
                return resposta.text
                
            except Exception as e:
                erro_str = str(e)
                
                if "429" in erro_str or "quota" in erro_str.lower() or "rate limit" in erro_str.lower():
                    if tentativa < max_tentativas - 1:
                        tempo_espera = 10 * (tentativa + 1)
                        time.sleep(tempo_espera)
                        continue
                    else:
                        return "Rick: *Arrota* Limite de cota excedido. That's just bureaucracy with extra steps!"
                else:
                    return f"Rick: *Arrota* Erro: {erro_str[:100]}"
        
        return "Rick: *Arrota* Não consegui resposta."


def main():
    """Função principal do programa"""
    print("\n" + "=" * 70)
    print("AGENTE RICK SANCHEZ - RICK AND MORTY")
    print("=" * 70)
    
    # Cria o agente Rick
    rick = AgenteRick()
    
    # Menu de opções
    print("\nEscolha uma opção:")
    print("1 - Conversar com o Rick (modo interativo)")
    print("2 - Fazer uma pergunta única")
    print("3 - Sair")
    
    opcao = input("\nOpção: ").strip()
    
    if opcao == "1":
        print("\n" + "=" * 70)
        rick.conversar()
        
    elif opcao == "2":
        pergunta = input("\nDigite sua pergunta: ").strip()
        if pergunta:
            print("\n" + "=" * 70)
            print("Rick: ", end="")
            resposta = rick.gerar_resposta_simples(pergunta)
            print(f"{resposta}")
            print("=" * 70)
            
    elif opcao == "3":
        print("\nRick: *Arrota* Fine, whatever.")
    else:
        print("\nRick: *Arrota* Opção inválida, Morty! Get your shit together!")


if __name__ == "__main__":
    main()


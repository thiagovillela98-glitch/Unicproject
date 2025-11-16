"""
Arquivo Principal - Projeto de Integração com API CEP Aberto
Trabalho de Faculdade - Validação e Integração entre APIs

Este projeto demonstra:
- Integração com API REST
- Validação de dados
- Tratamento de erros
- Manipulação de múltiplas requisições
- Exportação de dados (JSON e CSV)
"""

from cep_api import CepAbertoAPI
from config import API_TOKEN
import sys


def main():
    """Função principal do programa"""
    
    print("="*70)
    print("🗺️  PROJETO: INTEGRAÇÃO COM API CEP ABERTO")
    print("="*70)
    print("\n📚 Trabalho de Faculdade - Validação e Integração entre APIs")
    print("🔗 API: https://www.cepaberto.com/")
    print("\n" + "="*70)
    
    # Inicializa a API
    api = CepAbertoAPI(token=API_TOKEN)
    
    while True:
        print("\n📋 MENU PRINCIPAL:")
        print("   1 - Buscar um CEP")
        print("   2 - Buscar múltiplos CEPs")
        print("   3 - Buscar CEPs de capitais brasileiras")
        print("   4 - Buscar CEPs por região")
        print("   5 - Ver histórico de buscas")
        print("   6 - Ver estatísticas")
        print("   7 - Executar exemplos (demonstração completa)")
        print("   0 - Sair")
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "1":
            buscar_um_cep(api)
        elif escolha == "2":
            buscar_multiplos_ceps_usuario(api)
        elif escolha == "3":
            buscar_capitais(api)
        elif escolha == "4":
            buscar_por_regiao(api)
        elif escolha == "5":
            ver_historico(api)
        elif escolha == "6":
            ver_estatisticas(api)
        elif escolha == "7":
            executar_exemplos()
        elif escolha == "0":
            print("\n👋 Encerrando o programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")


def buscar_um_cep(api):
    """Busca um único CEP informado pelo usuário"""
    print("\n" + "="*70)
    print("🔍 BUSCAR UM CEP")
    print("="*70)
    
    cep = input("\n📮 Digite o CEP (com ou sem formatação): ").strip()
    
    if not cep:
        print("❌ CEP não pode estar vazio!")
        return
    
    print("\n🔎 Buscando...")
    resultado = api.buscar_cep(cep)
    
    if resultado:
        print("\n" + "="*70)
        print("📍 INFORMAÇÕES DO CEP")
        print("="*70)
        print(f"\n   CEP: {api.formatar_cep(resultado.get('cep', 'N/A'))}")
        print(f"   Logradouro: {resultado.get('logradouro', 'N/A')}")
        print(f"   Complemento: {resultado.get('complemento', 'N/A')}")
        print(f"   Bairro: {resultado.get('bairro', 'N/A')}")
        print(f"   Cidade: {resultado.get('cidade', {}).get('nome', 'N/A')}")
        print(f"   Estado: {resultado.get('estado', {}).get('sigla', 'N/A')}")
        print(f"   DDD: {resultado.get('cidade', {}).get('ddd', 'N/A')}")
        print(f"   IBGE: {resultado.get('cidade', {}).get('ibge', 'N/A')}")
        
        if resultado.get('latitude') and resultado.get('longitude'):
            print(f"\n   📍 Coordenadas:")
            print(f"      Latitude: {resultado.get('latitude')}")
            print(f"      Longitude: {resultado.get('longitude')}")
            print(f"      Altitude: {resultado.get('altitude', 'N/A')} metros")
        
        # Validação
        validacao = api.validar_dados_cep(resultado)
        print(f"\n   Status de Validação: {'✅ VÁLIDO' if validacao['valido'] else '⚠️  COM ALERTAS'}")
        
        # Perguntar se quer exportar
        exportar = input("\n💾 Deseja exportar este resultado? (s/n): ").strip().lower()
        if exportar == 's':
            api.exportar_resultados([resultado], f"cep_{resultado.get('cep')}.json")


def buscar_multiplos_ceps_usuario(api):
    """Busca múltiplos CEPs informados pelo usuário"""
    print("\n" + "="*70)
    print("🔍 BUSCAR MÚLTIPLOS CEPs")
    print("="*70)
    
    print("\n📝 Digite os CEPs separados por vírgula ou espaço:")
    print("   Exemplo: 01001000, 20040020, 30130100")
    
    entrada = input("\n📮 CEPs: ").strip()
    
    if not entrada:
        print("❌ Nenhum CEP informado!")
        return
    
    # Separa os CEPs
    ceps = [cep.strip() for cep in entrada.replace(",", " ").split() if cep.strip()]
    
    if not ceps:
        print("❌ Nenhum CEP válido informado!")
        return
    
    print(f"\n🔎 Buscando {len(ceps)} CEPs...")
    resultados = api.buscar_multiplos_ceps(ceps, intervalo=0.5)
    
    if resultados:
        # Pergunta se quer exportar
        exportar = input("\n💾 Deseja exportar os resultados? (s/n): ").strip().lower()
        if exportar == 's':
            api.exportar_resultados(resultados, "busca_multipla.json")
            
            exportar_csv = input("💾 Deseja exportar para CSV também? (s/n): ").strip().lower()
            if exportar_csv == 's':
                from exemplos import exportar_csv
                exportar_csv(resultados, "busca_multipla.csv")


def buscar_capitais(api):
    """Busca CEPs das capitais brasileiras"""
    print("\n" + "="*70)
    print("🏛️  BUSCAR CEPs DAS CAPITAIS BRASILEIRAS")
    print("="*70)
    
    capitais = {
        "São Paulo/SP": "01001000",
        "Rio de Janeiro/RJ": "20040020",
        "Belo Horizonte/MG": "30130100",
        "Salvador/BA": "40020000",
        "Fortaleza/CE": "60010000",
        "Brasília/DF": "70040902",
        "Curitiba/PR": "80010000",
        "Recife/PE": "50010000",
        "Porto Alegre/RS": "90010000",
        "Manaus/AM": "69005000",
        "Belém/PA": "66010000",
        "Goiânia/GO": "74003010",
        "Guarulhos/SP": "07010000",
        "Campinas/SP": "13010000",
        "São Luís/MA": "65010000",
    }
    
    print(f"\n📍 {len(capitais)} capitais serão consultadas")
    print("⏳ Isso pode levar alguns segundos...")
    
    confirmar = input("\n❓ Deseja continuar? (s/n): ").strip().lower()
    
    if confirmar != 's':
        print("❌ Operação cancelada.")
        return
    
    ceps = list(capitais.values())
    resultados = api.buscar_multiplos_ceps(ceps, intervalo=0.5)
    
    if resultados:
        print("\n✅ Busca concluída!")
        exportar = input("\n💾 Deseja exportar os resultados? (s/n): ").strip().lower()
        if exportar == 's':
            api.exportar_resultados(resultados, "capitais_brasil.json")
            from exemplos import exportar_csv
            exportar_csv(resultados, "capitais_brasil.csv")


def buscar_por_regiao(api):
    """Busca CEPs organizados por região"""
    print("\n" + "="*70)
    print("🗺️  BUSCAR CEPs POR REGIÃO")
    print("="*70)
    
    print("\n📍 Regiões disponíveis:")
    print("   1 - Sudeste")
    print("   2 - Sul")
    print("   3 - Nordeste")
    print("   4 - Norte")
    print("   5 - Centro-Oeste")
    
    escolha = input("\n👉 Escolha uma região: ").strip()
    
    ceps_regioes = {
        "1": {
            "nome": "Sudeste",
            "ceps": ["01001000", "20040020", "30130100", "29010000"]  # SP, RJ, MG, ES
        },
        "2": {
            "nome": "Sul",
            "ceps": ["80010000", "90010000", "88010000"]  # PR, RS, SC
        },
        "3": {
            "nome": "Nordeste",
            "ceps": ["40020000", "50010000", "60010000", "57020000"]  # BA, PE, CE, AL
        },
        "4": {
            "nome": "Norte",
            "ceps": ["69005000", "66010000", "78010000"]  # AM, PA, MT
        },
        "5": {
            "nome": "Centro-Oeste",
            "ceps": ["70040902", "74003010", "79002000"]  # DF, GO, MS
        }
    }
    
    if escolha not in ceps_regioes:
        print("❌ Região inválida!")
        return
    
    regiao = ceps_regioes[escolha]
    print(f"\n🔍 Buscando CEPs da região {regiao['nome']}...")
    
    resultados = api.buscar_multiplos_ceps(regiao['ceps'], intervalo=0.5)
    
    if resultados:
        exportar = input("\n💾 Deseja exportar os resultados? (s/n): ").strip().lower()
        if exportar == 's':
            nome_arquivo = f"regiao_{regiao['nome'].lower()}.json"
            api.exportar_resultados(resultados, nome_arquivo)


def ver_historico(api):
    """Mostra o histórico de buscas"""
    print("\n" + "="*70)
    print("📜 HISTÓRICO DE BUSCAS")
    print("="*70)
    
    historico = api.obter_historico()
    
    if not historico:
        print("\n⚠️  Nenhuma busca realizada ainda.")
        return
    
    print(f"\n📊 Total de buscas: {len(historico)}\n")
    
    for idx, busca in enumerate(historico, 1):
        status_icon = "✅" if busca['status'] == 200 else "❌"
        print(f"{idx}. {status_icon} CEP: {api.formatar_cep(busca['cep'])} | "
              f"Status: {busca['status']} | "
              f"Horário: {busca['timestamp']}")


def ver_estatisticas(api):
    """Mostra estatísticas das buscas"""
    print("\n" + "="*70)
    print("📊 ESTATÍSTICAS DE BUSCAS")
    print("="*70)
    
    stats = api.obter_estatisticas()
    
    print(f"\n   📈 Total de buscas realizadas: {stats['total_buscas']}")
    print(f"   ✅ Buscas bem-sucedidas: {stats['buscas_sucesso']}")
    print(f"   ❌ Buscas com erro: {stats['buscas_erro']}")
    print(f"   📊 Taxa de sucesso: {stats['taxa_sucesso']}%")


def executar_exemplos():
    """Executa o arquivo de exemplos"""
    print("\n" + "="*70)
    print("🚀 EXECUTANDO EXEMPLOS DE DEMONSTRAÇÃO")
    print("="*70)
    
    try:
        from exemplos import menu_interativo
        menu_interativo()
    except ImportError as e:
        print(f"❌ Erro ao importar exemplos: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)


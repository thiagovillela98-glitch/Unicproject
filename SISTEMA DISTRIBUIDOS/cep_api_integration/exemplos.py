"""
Exemplos de uso da API CEP Aberto
Demonstra diferentes formas de buscar e validar CEPs
"""

from cep_api import CepAbertoAPI
import csv
from datetime import datetime


def exemplo_busca_simples():
    """Exemplo 1: Busca simples de um CEP"""
    print("\n" + "="*60)
    print("EXEMPLO 1: Busca Simples de CEP")
    print("="*60)
    
    # Inicializa a API com seu token
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    # Busca um CEP específico
    cep = "01001000"  # Praça da Sé, São Paulo
    resultado = api.buscar_cep(cep)
    
    if resultado:
        print(f"\n📍 Endereço completo:")
        print(f"   Logradouro: {resultado.get('logradouro')}")
        print(f"   Bairro: {resultado.get('bairro')}")
        print(f"   Cidade: {resultado.get('cidade', {}).get('nome')}")
        print(f"   Estado: {resultado.get('estado', {}).get('sigla')}")
        print(f"   CEP: {api.formatar_cep(resultado.get('cep'))}")


def exemplo_multiplos_ceps():
    """Exemplo 2: Busca múltiplos CEPs de diferentes regiões"""
    print("\n" + "="*60)
    print("EXEMPLO 2: Busca de Múltiplos CEPs (Diversas Regiões)")
    print("="*60)
    
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    # Lista de CEPs de diferentes estados do Brasil
    ceps_brasil = [
        "01001000",  # São Paulo/SP - Praça da Sé
        "20040020",  # Rio de Janeiro/RJ - Centro
        "30130100",  # Belo Horizonte/MG - Centro
        "40020000",  # Salvador/BA - Centro
        "50010000",  # Recife/PE - Recife
        "60010000",  # Fortaleza/CE - Centro
        "70040902",  # Brasília/DF - Esplanada dos Ministérios
        "80010000",  # Curitiba/PR - Centro
        "90010000",  # Porto Alegre/RS - Centro
        "69005000",  # Manaus/AM - Centro
    ]
    
    # Busca todos os CEPs
    resultados = api.buscar_multiplos_ceps(ceps_brasil, intervalo=0.5)
    
    # Exibe estatísticas
    stats = api.obter_estatisticas()
    print(f"\n📊 ESTATÍSTICAS:")
    print(f"   Total de buscas: {stats['total_buscas']}")
    print(f"   Buscas com sucesso: {stats['buscas_sucesso']}")
    print(f"   Buscas com erro: {stats['buscas_erro']}")
    print(f"   Taxa de sucesso: {stats['taxa_sucesso']}%")
    
    return resultados


def exemplo_validacao_dados():
    """Exemplo 3: Validação de dados retornados pela API"""
    print("\n" + "="*60)
    print("EXEMPLO 3: Validação de Dados da API")
    print("="*60)
    
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    ceps_teste = ["01001000", "20040020", "30130100"]
    
    for cep in ceps_teste:
        print(f"\n🔍 Validando CEP: {cep}")
        dados = api.buscar_cep(cep)
        
        if dados:
            validacao = api.validar_dados_cep(dados)
            
            print(f"   Status: {'✅ VÁLIDO' if validacao['valido'] else '❌ INVÁLIDO'}")
            print(f"   Campos presentes: {len(validacao['campos_presentes'])}")
            print(f"   Campos ausentes: {len(validacao['campos_ausentes'])}")
            
            if validacao['alertas']:
                print(f"   ⚠️  Alertas:")
                for alerta in validacao['alertas']:
                    print(f"      - {alerta}")


def exemplo_exportar_resultados():
    """Exemplo 4: Exportar resultados para arquivo"""
    print("\n" + "="*60)
    print("EXEMPLO 4: Exportação de Resultados")
    print("="*60)
    
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    # CEPs de capitais brasileiras
    ceps_capitais = [
        "01001000",  # São Paulo/SP
        "20040020",  # Rio de Janeiro/RJ
        "30130100",  # Belo Horizonte/MG
        "40020000",  # Salvador/BA
        "50010000",  # Recife/PE
        "60010000",  # Fortaleza/CE
        "70040902",  # Brasília/DF
        "80010000",  # Curitiba/PR
    ]
    
    print("\n🔍 Buscando CEPs das capitais...")
    resultados = api.buscar_multiplos_ceps(ceps_capitais, intervalo=0.5)
    
    # Exporta para JSON
    api.exportar_resultados(resultados, "ceps_capitais.json")
    
    # Exporta para CSV
    exportar_csv(resultados, "ceps_capitais.csv")


def exportar_csv(resultados, arquivo):
    """Exporta resultados para CSV"""
    try:
        with open(arquivo, 'w', newline='', encoding='utf-8-sig') as f:
            if not resultados:
                print("⚠️  Nenhum resultado para exportar")
                return
            
            writer = csv.writer(f)
            
            # Cabeçalho
            writer.writerow([
                'CEP', 'Logradouro', 'Complemento', 'Bairro', 
                'Cidade', 'UF', 'DDD', 'Latitude', 'Longitude', 'Altitude'
            ])
            
            # Dados
            for resultado in resultados:
                writer.writerow([
                    resultado.get('cep', ''),
                    resultado.get('logradouro', ''),
                    resultado.get('complemento', ''),
                    resultado.get('bairro', ''),
                    resultado.get('cidade', {}).get('nome', ''),
                    resultado.get('estado', {}).get('sigla', ''),
                    resultado.get('cidade', {}).get('ddd', ''),
                    resultado.get('latitude', ''),
                    resultado.get('longitude', ''),
                    resultado.get('altitude', '')
                ])
        
        print(f"✅ Resultados exportados para {arquivo}")
    except Exception as e:
        print(f"❌ Erro ao exportar CSV: {str(e)}")


def exemplo_ceps_por_estado():
    """Exemplo 5: Buscar CEPs organizados por estado"""
    print("\n" + "="*60)
    print("EXEMPLO 5: CEPs por Estado (Região Sudeste)")
    print("="*60)
    
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    # CEPs do Sudeste
    ceps_sudeste = {
        "São Paulo": ["01001000", "01310100", "04101000"],
        "Rio de Janeiro": ["20040020", "22250040", "23550020"],
        "Minas Gerais": ["30130100", "30190020", "31110020"],
        "Espírito Santo": ["29010000", "29060000", "29100000"]
    }
    
    resultados_por_estado = {}
    
    for estado, ceps in ceps_sudeste.items():
        print(f"\n📍 Estado: {estado}")
        print(f"   Buscando {len(ceps)} CEPs...")
        resultados = api.buscar_multiplos_ceps(ceps, intervalo=0.5)
        resultados_por_estado[estado] = resultados
        print(f"   ✅ {len(resultados)} CEPs encontrados")
    
    return resultados_por_estado


def exemplo_tratamento_erros():
    """Exemplo 6: Tratamento de erros e CEPs inválidos"""
    print("\n" + "="*60)
    print("EXEMPLO 6: Tratamento de Erros")
    print("="*60)
    
    api = CepAbertoAPI(token="2682d07a7ba75ae182dd575a51dc6504")
    
    # Lista com CEPs válidos e inválidos
    ceps_teste = [
        "01001000",     # ✅ Válido
        "99999999",     # ❓ Pode não existir
        "00000000",     # ❓ Pode não existir
        "123",          # ❌ Formato inválido
        "abcdefgh",     # ❌ Formato inválido
        "12345-678",    # ✅ Válido com formatação
    ]
    
    print("\n🔍 Testando CEPs válidos e inválidos:\n")
    
    for cep in ceps_teste:
        print(f"\nTestando: {cep}")
        resultado = api.buscar_cep(cep)
        
        if resultado:
            print(f"   ✅ Encontrado: {resultado.get('logradouro', 'N/A')}")
        else:
            print(f"   ❌ Não encontrado ou inválido")


def menu_interativo():
    """Menu interativo para testar a API"""
    print("\n" + "="*60)
    print("🗺️  SISTEMA DE BUSCA DE CEPs - API CEP ABERTO")
    print("="*60)
    
    while True:
        print("\n📋 MENU DE EXEMPLOS:")
        print("   1 - Busca Simples de CEP")
        print("   2 - Buscar Múltiplos CEPs (Capitais)")
        print("   3 - Validação de Dados")
        print("   4 - Exportar Resultados (JSON e CSV)")
        print("   5 - CEPs por Estado (Sudeste)")
        print("   6 - Tratamento de Erros")
        print("   7 - Executar TODOS os exemplos")
        print("   0 - Sair")
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "1":
            exemplo_busca_simples()
        elif escolha == "2":
            exemplo_multiplos_ceps()
        elif escolha == "3":
            exemplo_validacao_dados()
        elif escolha == "4":
            exemplo_exportar_resultados()
        elif escolha == "5":
            exemplo_ceps_por_estado()
        elif escolha == "6":
            exemplo_tratamento_erros()
        elif escolha == "7":
            print("\n🚀 Executando todos os exemplos...\n")
            exemplo_busca_simples()
            exemplo_multiplos_ceps()
            exemplo_validacao_dados()
            exemplo_exportar_resultados()
            exemplo_ceps_por_estado()
            exemplo_tratamento_erros()
            print("\n✅ Todos os exemplos executados!")
        elif escolha == "0":
            print("\n👋 Encerrando o programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
        
        input("\n⏸️  Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu_interativo()


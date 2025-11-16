"""
Teste Rápido - Verifica se a API está funcionando
Execute este arquivo para testar rapidamente a conexão com a API
"""

from cep_api import CepAbertoAPI
from config import API_TOKEN


def teste_basico():
    """Teste básico de funcionamento da API"""
    print("="*70)
    print("🧪 TESTE RÁPIDO DA API CEP ABERTO")
    print("="*70)
    
    print("\n1️⃣  Inicializando API...")
    try:
        api = CepAbertoAPI(token=API_TOKEN)
        print("   ✅ API inicializada com sucesso!")
    except Exception as e:
        print(f"   ❌ Erro ao inicializar API: {e}")
        return False
    
    print("\n2️⃣  Testando busca de CEP (01001-000 - Praça da Sé, SP)...")
    try:
        resultado = api.buscar_cep("01001000")
        
        if resultado:
            print("   ✅ CEP encontrado com sucesso!")
            print(f"\n   📍 Dados retornados:")
            print(f"      CEP: {resultado.get('cep')}")
            print(f"      Logradouro: {resultado.get('logradouro')}")
            print(f"      Bairro: {resultado.get('bairro')}")
            print(f"      Cidade: {resultado.get('cidade', {}).get('nome')}")
            print(f"      Estado: {resultado.get('estado', {}).get('sigla')}")
        else:
            print("   ❌ CEP não encontrado ou erro na busca")
            print("   ⚠️  Verifique:")
            print("      - Seu token está correto?")
            print("      - Você tem conexão com internet?")
            print("      - O limite de requisições foi atingido?")
            return False
    except Exception as e:
        print(f"   ❌ Erro ao buscar CEP: {e}")
        return False
    
    print("\n3️⃣  Testando validação de dados...")
    try:
        validacao = api.validar_dados_cep(resultado)
        if validacao['valido']:
            print("   ✅ Dados validados com sucesso!")
            print(f"      Campos presentes: {len(validacao['campos_presentes'])}")
        else:
            print("   ⚠️  Dados com alertas:")
            for alerta in validacao['alertas']:
                print(f"      - {alerta}")
    except Exception as e:
        print(f"   ❌ Erro ao validar dados: {e}")
        return False
    
    print("\n4️⃣  Testando estatísticas...")
    try:
        stats = api.obter_estatisticas()
        print("   ✅ Estatísticas obtidas:")
        print(f"      Total de buscas: {stats['total_buscas']}")
        print(f"      Taxa de sucesso: {stats['taxa_sucesso']}%")
    except Exception as e:
        print(f"   ❌ Erro ao obter estatísticas: {e}")
        return False
    
    print("\n" + "="*70)
    print("✅ TODOS OS TESTES PASSARAM!")
    print("="*70)
    print("\n🚀 Você pode agora executar:")
    print("   - python main.py (programa principal)")
    print("   - python exemplos.py (exemplos de uso)")
    print("\n")
    
    return True


if __name__ == "__main__":
    try:
        sucesso = teste_basico()
        
        if not sucesso:
            print("\n" + "="*70)
            print("❌ ALGUNS TESTES FALHARAM")
            print("="*70)
            print("\n💡 Dicas:")
            print("   1. Verifique seu token em config.py")
            print("   2. Confirme sua conexão com internet")
            print("   3. Veja a documentação em README.md")
            print("\n")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Teste interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


"""
Módulo de Integração com API CEP Aberto
Desenvolvido para validação e integração entre APIs
"""

import requests
import json
import time
from typing import Dict, List, Optional
from datetime import datetime


class CepAbertoAPI:
    """
    Classe para integração com a API CEP Aberto
    Permite buscar e validar CEPs de todo o Brasil
    """
    
    BASE_URL = "https://www.cepaberto.com/api/v3"
    
    def __init__(self, token: str):
        """
        Inicializa a conexão com a API
        
        Args:
            token (str): Token de autenticação da API CEP Aberto
        """
        self.token = token
        self.headers = {'Authorization': f'Token token={token}'}
        self.historico_buscas = []
    
    def buscar_cep(self, cep: str) -> Optional[Dict]:
        """
        Busca informações de um CEP específico
        
        Args:
            cep (str): CEP a ser buscado (com ou sem formatação)
            
        Returns:
            Dict: Dicionário com informações do CEP ou None em caso de erro
        """
        # Remove formatação do CEP (hífens e espaços)
        cep_limpo = cep.replace("-", "").replace(".", "").replace(" ", "")
        
        # Valida o formato do CEP
        if not self._validar_formato_cep(cep_limpo):
            print(f"❌ CEP inválido: {cep}")
            return None
        
        url = f"{self.BASE_URL}/cep?cep={cep_limpo}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            # Registra a busca no histórico
            self._adicionar_historico(cep_limpo, response.status_code)
            
            if response.status_code == 200:
                dados = response.json()
                print(f"✅ CEP {cep_limpo} encontrado: {dados.get('logradouro', 'N/A')}, {dados.get('bairro', 'N/A')} - {dados.get('cidade', {}).get('nome', 'N/A')}/{dados.get('estado', {}).get('sigla', 'N/A')}")
                return dados
            elif response.status_code == 404:
                print(f"⚠️  CEP {cep_limpo} não encontrado na base de dados")
                return None
            elif response.status_code == 401:
                print(f"❌ Erro de autenticação. Verifique seu token.")
                return None
            elif response.status_code == 429:
                print(f"⚠️  Limite de requisições excedido. Aguarde um momento...")
                return None
            else:
                print(f"❌ Erro ao buscar CEP {cep_limpo}: Status {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print(f"⏱️  Timeout ao buscar CEP {cep_limpo}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão ao buscar CEP {cep_limpo}: {str(e)}")
            return None
    
    def buscar_multiplos_ceps(self, lista_ceps: List[str], intervalo: float = 1.0) -> List[Dict]:
        """
        Busca múltiplos CEPs com intervalo entre requisições
        
        Args:
            lista_ceps (List[str]): Lista de CEPs a serem buscados
            intervalo (float): Intervalo em segundos entre cada requisição
            
        Returns:
            List[Dict]: Lista com os dados dos CEPs encontrados
        """
        resultados = []
        total = len(lista_ceps)
        
        print(f"\n🔍 Iniciando busca de {total} CEPs...\n")
        
        for idx, cep in enumerate(lista_ceps, 1):
            print(f"[{idx}/{total}] ", end="")
            resultado = self.buscar_cep(cep)
            
            if resultado:
                resultados.append(resultado)
            
            # Aguarda intervalo entre requisições (exceto na última)
            if idx < total:
                time.sleep(intervalo)
        
        print(f"\n✅ Busca concluída! {len(resultados)} CEPs encontrados de {total} buscados.\n")
        return resultados
    
    def validar_dados_cep(self, dados_cep: Dict) -> Dict:
        """
        Valida os dados retornados pela API
        
        Args:
            dados_cep (Dict): Dados do CEP retornados pela API
            
        Returns:
            Dict: Relatório de validação
        """
        validacao = {
            'valido': True,
            'alertas': [],
            'campos_presentes': [],
            'campos_ausentes': []
        }
        
        campos_obrigatorios = ['cep', 'logradouro', 'bairro', 'cidade', 'estado']
        campos_opcionais = ['altitude', 'longitude', 'latitude', 'complemento']
        
        # Verifica campos obrigatórios
        for campo in campos_obrigatorios:
            if campo in dados_cep and dados_cep[campo]:
                validacao['campos_presentes'].append(campo)
            else:
                validacao['campos_ausentes'].append(campo)
                validacao['alertas'].append(f"Campo obrigatório ausente: {campo}")
                validacao['valido'] = False
        
        # Verifica campos opcionais
        for campo in campos_opcionais:
            if campo in dados_cep and dados_cep[campo]:
                validacao['campos_presentes'].append(campo)
        
        # Validações específicas
        if 'cidade' in dados_cep:
            if not isinstance(dados_cep['cidade'], dict):
                validacao['alertas'].append("Campo 'cidade' não está no formato esperado")
                validacao['valido'] = False
            elif 'nome' not in dados_cep['cidade']:
                validacao['alertas'].append("Nome da cidade não encontrado")
                validacao['valido'] = False
        
        if 'estado' in dados_cep:
            if not isinstance(dados_cep['estado'], dict):
                validacao['alertas'].append("Campo 'estado' não está no formato esperado")
                validacao['valido'] = False
            elif 'sigla' not in dados_cep['estado']:
                validacao['alertas'].append("Sigla do estado não encontrada")
                validacao['valido'] = False
        
        return validacao
    
    def _validar_formato_cep(self, cep: str) -> bool:
        """
        Valida o formato do CEP (deve ter 8 dígitos numéricos)
        
        Args:
            cep (str): CEP a ser validado
            
        Returns:
            bool: True se válido, False caso contrário
        """
        return len(cep) == 8 and cep.isdigit()
    
    def _adicionar_historico(self, cep: str, status_code: int):
        """
        Adiciona uma busca ao histórico
        
        Args:
            cep (str): CEP buscado
            status_code (int): Código de status da resposta
        """
        self.historico_buscas.append({
            'cep': cep,
            'status': status_code,
            'timestamp': datetime.now().isoformat()
        })
    
    def obter_historico(self) -> List[Dict]:
        """
        Retorna o histórico de buscas realizadas
        
        Returns:
            List[Dict]: Lista com histórico de buscas
        """
        return self.historico_buscas
    
    def obter_estatisticas(self) -> Dict:
        """
        Retorna estatísticas sobre as buscas realizadas
        
        Returns:
            Dict: Dicionário com estatísticas
        """
        if not self.historico_buscas:
            return {
                'total_buscas': 0,
                'buscas_sucesso': 0,
                'buscas_erro': 0,
                'taxa_sucesso': 0.0
            }
        
        total = len(self.historico_buscas)
        sucessos = sum(1 for b in self.historico_buscas if b['status'] == 200)
        erros = total - sucessos
        taxa = (sucessos / total) * 100 if total > 0 else 0
        
        return {
            'total_buscas': total,
            'buscas_sucesso': sucessos,
            'buscas_erro': erros,
            'taxa_sucesso': round(taxa, 2)
        }
    
    def exportar_resultados(self, resultados: List[Dict], arquivo: str = "resultados_cep.json"):
        """
        Exporta resultados para um arquivo JSON
        
        Args:
            resultados (List[Dict]): Lista de resultados a serem exportados
            arquivo (str): Nome do arquivo de saída
        """
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(resultados, f, ensure_ascii=False, indent=2)
            print(f"✅ Resultados exportados para {arquivo}")
        except Exception as e:
            print(f"❌ Erro ao exportar resultados: {str(e)}")
    
    def formatar_cep(self, cep: str) -> str:
        """
        Formata o CEP no padrão XXXXX-XXX
        
        Args:
            cep (str): CEP sem formatação
            
        Returns:
            str: CEP formatado
        """
        cep_limpo = cep.replace("-", "").replace(".", "").replace(" ", "")
        if len(cep_limpo) == 8:
            return f"{cep_limpo[:5]}-{cep_limpo[5:]}"
        return cep


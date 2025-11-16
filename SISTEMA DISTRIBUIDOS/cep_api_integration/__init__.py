"""
Projeto de Integração com API CEP Aberto
Trabalho de Faculdade - Validação e Integração entre APIs
"""

__version__ = "1.0.0"
__author__ = "Trabalho de Faculdade"
__description__ = "Integração com API CEP Aberto para busca e validação de CEPs do Brasil"

from .cep_api import CepAbertoAPI

__all__ = ['CepAbertoAPI']


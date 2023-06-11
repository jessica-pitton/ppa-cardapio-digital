import sys

if hasattr(sys, 'real_prefix'):
    # O ambiente virtual está ativado
    print("Ambiente virtual ativo:", sys.prefix)
else:
    # O ambiente virtual não está ativado
    print("Nenhum ambiente virtual ativo.")


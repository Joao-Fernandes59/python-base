#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__ = "0.1.0"

""""
produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None
"""
from pprint import pprint
produto = {
	"nome": "Caneta",
#	"cor1": "azul",  => substituída por uma lista
#	"cor2": "branco",
    "cores": ["azul", "branco"],
	"preco": 3.23,
#	"dimensao_altura": 12.1, => substituída por um dicionário
#	"dimensao_largura":  0.8,
    "dimensao":{"altura": 12.1, "largura": 0.8
    },
	"em_estoque": True,
	"codigo": 45678,
	"codebar": None,
}
#Agora temos um único objeto 

# compra = ("Bruno", produto["nome"], 3) => substituída por um 2 dicionários
cliente = {"nome": "Bruno"
}
compra = {"cliente": cliente, 
          "produto": produto, 
          "quantidade": 3
}

# pprint(compra)


total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}")

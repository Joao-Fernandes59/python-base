#!/usr/bin/env puthon3
"""Calculadora prefix.

Funcinamento:

[operação] [n1] [n2]

Operações
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py  (caso o usuário não informe os argumentos)
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em 'prefixcalc.log'
"""
__version__ = "0.1.0"

import os
import sys

from datetime import datetime

while True:

    arguments = sys.argv[1:]

    # Validação Normal
    if not arguments:
        operation = input("Operação:")
        n1        = input("n1:")
        n2        = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Números de argumentos inválidos")
        print("Ex: 'sum 5 5'")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Erro!! - Operação inválida")
        print(f"Operações válidas: {valid_operations}")
        sys.exit(1)
        
    validated_nums = []                
    for num in nums:
        # TODO: Repetição while + exceptions
        if not num.replace(".", "").isdigit():
            print(f"Número invalido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    # Abordagem EAFP
    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    #TODO: Usar dict de funções
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2  # Se for //, e reultado será exibido inteiro

    print(f"O resultado é: {result}")

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv("USERNAME", 'anonymous')

    # Abordagem EAFP
    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        #TODO: logging
        print(str(e))
        sys.exit(1)

    # print(f"{operation}, {n1}, {n2} = {result}", file=open(filepath, "a"))
    if input("Pressione enter para continuar ou qualquer tecla para sair. "):
        break

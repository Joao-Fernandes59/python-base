#!/usr/bin/env python3
""" Hello World Multi Línguas.

Dependendo da língua configurada no ambiente, o programa exibe a mensagem 
correspondente.

Como usar: 

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

OU informe através do CLI argument '--lang'

Ou o usuário tera que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__  = "João Fernandes"
__license__ = "UNlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    """ Abordagem com LBYL
    if "=" in arg:
        key, value = arg.split("=")
    else:
        print("You need to use '='")
        sys.exit(1)
    """
    # Abordagem com EAFP
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Substitui por logging
        print(f"[ERRO] {str(e)}")
        print("You need to use '='")
        print(f"You passed {arg}")
        print("Try with --key=value")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    # Operação de validação normal
    if key not in arguments:
        print(f"Invalida Option '{key}'")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

#msg = "Hello, World!"
msg = {
   "en_US": "Hello World!",
   "pt_BR": "Olá, Mundo!",
   "it_IT": "Ciao, Mondo!",
   "es_SP": "Hola, Mundo!",
   "fr_FR": "Bonjour le monde!",
}

# sets (Hash Table) - O(1) - constante
# dict (hash Table) - O(1) - constante

"""
# Ordem Complexidade O(n)
if current_language   == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour le monde!"
"""

#print(msg) 

# 0(1) - constante - 'in'

# Abordagem LBYL
"""if current_language in msg:
    message = msg[current_language]
else:
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)
"""
# Abordagem EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERRO] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

# try com valor default         NÃO RECOMENDADO
#message = msg.get(current_language, msg["en_US"])

print(
    message * int(arguments["count"])
)

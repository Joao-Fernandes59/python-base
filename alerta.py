"""
Alarme de temparatura

Faça um script que pergunta ao usuário qual a temparatura atual e o índice de
umiudade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

Se temperatura maior que 45: ALERTA!!! Perigo de calor extremo
Senão, se temperatura vezes 3 maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
Senão, se temparatura entre 10 e 30: Normal
Senão, se temperatura entre 0 e 10: Frio
Senão, se temperatura <0: ALERTA: Frio extremo
"""

import sys
import logging
log = logging.Logger("alerta")
# TODO: Customizar o log

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual é a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!!! 🥵 Perigo de calor extremo")
elif temp * 3 >= umidade: # pemdas.info (Regras de precedências)
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("🙂 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ⛄ Frio extremo")




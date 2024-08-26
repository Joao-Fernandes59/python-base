#!/usr/bin/env python3

import os
import logging
from logging import handlers

#-> Configuração do log - BOILERPLATE
# O usuário pode configurar o level de mensagem que deseja receber
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# Nossa Instancia
# TODO: Usar função para utilizar em outros projetos
# TODO: Depois passar a usar a lib (loguru)
log = logging.Logger("joao_fernandes", log_level) # setup do nível de log
# Level / Handler reesponsável para enviar para o console
# ch = logging.StreamHandler()   # Determinar onde mensagem será exibida (Console/Terminal/stderr)
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, # 10**6 => 1 MB 
    backupCount=10) 
fh.setLevel(log_level)
# Formatação - Definir qual o formato que a mensagem será exibida na tela
"""ONDE:
%(asctime)s     -> Hora atual do acontecimento do evento
%(name)s        -> Nome do log
%(levelname)s   -> O nível do log (Ex. DEBUG)
l:%(lineno)d    -> Número da linha onde a mensagem ocorreu
f:%(filename)s: -> Nome do arquivo
%(message)s     -> A mensagem
"""
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)    
#ch.setFormatter(fmt) # insere o objeto de formatação dentro do Handler
fh.setFormatter(fmt) # insere o objeto de formatação dentro do Handler
# Destino
#log.addHandler(ch) # Adiciona o Handler ao log
log.addHandler(fh) # Adiciona o Handler ao log


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de Dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro! %s", str(e))
    # print(f"[ERRO] Deu erro! {str(e)}")
    
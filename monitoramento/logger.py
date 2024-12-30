import logging

class EventoLogger:
    def __init__(self, nome_arquivo):
        self.logger = logging.getLogger(nome_arquivo)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(nome_arquivo)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)

    def registrar_evento(self, evento):
        self.logger.info(evento)
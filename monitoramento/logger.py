import logging

class EventoLogger:
    def __init__(self, nome_arquivo):
        self.logger = logging.getLogger(nome_arquivo)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f'logs/{nome_arquivo}')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)

    def registrar_evento(self, evento):
        self.logger.info(evento)

    @staticmethod
    def configurar_logger_principal():
        logger = logging.getLogger('monitoramento')
        handler = logging.FileHandler('logs/monitoramento.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
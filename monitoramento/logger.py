import logging
import os

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
        if not os.path.exists('logs'):
            os.makedirs('logs')

        logger = logging.getLogger('monitoramento')
        handler = logging.FileHandler('logs/monitoramento.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def fechar_loggers():
        loggers = ['monitoramento', 'teclado_eventos.log', 'mouse_eventos.log', 'ociosidade_eventos.log']
        for logger_name in loggers:
            logger = logging.getLogger(logger_name)
            for handler in logger.handlers:
                handler.close()
            logger.handlers = []
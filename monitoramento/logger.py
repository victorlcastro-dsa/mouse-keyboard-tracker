import logging
import os
from .config import Config

class EventoLogger:
    def __init__(self, nome_arquivo):
        self.logger = self._configurar_logger(nome_arquivo, f'{Config.LOG_DIR}/{nome_arquivo}')

    def registrar_evento(self, evento):
        """Registra um evento no logger."""
        self.logger.info(evento)

    @staticmethod
    def _configurar_logger(nome, caminho_arquivo):
        """Configura um logger com o nome e caminho de arquivo especificados."""
        logger = logging.getLogger(nome)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(caminho_arquivo)
        handler.setFormatter(logging.Formatter(Config.LOG_FORMAT))
        logger.addHandler(handler)
        return logger

    @staticmethod
    def _configurar_diretorio_log():
        """Configura o diretório de logs se não existir."""
        if not os.path.exists(Config.LOG_DIR):
            os.makedirs(Config.LOG_DIR)

    @staticmethod
    def configurar_logger_principal():
        """Configura o logger principal."""
        EventoLogger._configurar_diretorio_log()
        return EventoLogger._configurar_logger('monitoramento', f'{Config.LOG_DIR}/monitoramento.log')

    @staticmethod
    def fechar_loggers():
        """Fecha todos os loggers configurados."""
        loggers = ['monitoramento', 'teclado_eventos.log', 'mouse_eventos.log', 'ociosidade_eventos.log']
        for logger_name in loggers:
            logger = logging.getLogger(logger_name)
            for handler in logger.handlers:
                handler.close()
            logger.handlers = []
import time
from monitoramento.logger import EventoLogger

class MonitorOciosidade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MonitorOciosidade, cls).__new__(cls)
        return cls._instance

    def __init__(self, tempo_maximo_ocioso=600):
        if not hasattr(self, 'initialized'):
            self.tempo_maximo_ocioso = tempo_maximo_ocioso
            self.ultimo_evento = time.time()
            self.ociosidade_logger = EventoLogger('ociosidade_eventos.log')
            self.initialized = True

    def atualizar_ultimo_evento(self):
        self.ultimo_evento = time.time()

    def verificar_ociosidade(self):
        while True:
            tempo_atual = time.time()
            if tempo_atual - self.ultimo_evento > self.tempo_maximo_ocioso:
                evento = f"O usuário está ocioso por mais de {self.tempo_maximo_ocioso} segundos."
                self.ociosidade_logger.registrar_evento(evento)
            time.sleep(1)
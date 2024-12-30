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
            self.ocioso = False
            self.initialized = True

    def atualizar_ultimo_evento(self):
        self.ultimo_evento = time.time()
        self.ocioso = False

    def verificar_ociosidade(self):
        while True:
            tempo_atual = time.time()
            tempo_ocioso = tempo_atual - self.ultimo_evento
            if tempo_ocioso > self.tempo_maximo_ocioso:
                if not self.ocioso:
                    self.ocioso = True
                    evento = f"O usuário está ocioso desde {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.ultimo_evento))}."
                    self.ociosidade_logger.registrar_evento(evento)
                else:
                    evento = f"O usuário está ocioso há {int(tempo_ocioso)} segundos."
                    self.ociosidade_logger.registrar_evento(evento)
            time.sleep(1)
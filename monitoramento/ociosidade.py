import time
from monitoramento.logger import EventoLogger
from monitoramento.config import Config

class MonitorOciosidade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MonitorOciosidade, cls).__new__(cls)
        return cls._instance

    def __init__(self, tempo_maximo_ocioso=Config.TEMPO_MAXIMO_OCIOSO):
        if not hasattr(self, 'initialized'):
            self.tempo_maximo_ocioso = tempo_maximo_ocioso
            self.ultimo_evento = time.time()
            self.ociosidade_logger = EventoLogger('ociosidade_eventos.log')
            self.ocioso = False
            self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO
            self.tempo_ocioso_total = Config.TEMPO_OCIOSO_TOTAL
            self.initialized = True

    def atualizar_ultimo_evento(self):
        if self.ocioso:
            tempo_ocioso = time.time() - self.ultimo_evento
            horas, resto = divmod(tempo_ocioso, Config.SEGUNDOS_EM_UMA_HORA)
            minutos, segundos = divmod(resto, Config.SEGUNDOS_EM_UM_MINUTO)
            evento = f"O usuário esteve ocioso por {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos."
            self.ociosidade_logger.registrar_evento(evento)
            self.tempo_ocioso_total += tempo_ocioso
        self.ultimo_evento = time.time()
        self.ocioso = False
        self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO

    def verificar_ociosidade(self):
        while True:
            tempo_atual = time.time()
            tempo_ocioso = tempo_atual - self.ultimo_evento
            if tempo_ocioso > self.tempo_maximo_ocioso:
                if not self.ocioso:
                    self.ocioso = True
                    evento = f"O usuário está ocioso desde {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.ultimo_evento))}."
                    self.ociosidade_logger.registrar_evento(evento)
                self.tempo_ocioso_acumulado = tempo_ocioso
            else:
                if self.ocioso:
                    evento = f"O usuário esteve ocioso por {int(self.tempo_ocioso_acumulado)} segundos."
                    self.ociosidade_logger.registrar_evento(evento)
                    self.ocioso = False
                    self.tempo_ocioso_total += self.tempo_ocioso_acumulado
                    self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO
            time.sleep(Config.INTERVALO_CHECAGEM_OCIOSIDADE)

    def registrar_tempo_total_ociosidade(self):
        horas, resto = divmod(self.tempo_ocioso_total, Config.SEGUNDOS_EM_UMA_HORA)
        minutos, segundos = divmod(resto, Config.SEGUNDOS_EM_UM_MINUTO)
        evento = f"Tempo total de ociosidade: {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos."
        self.ociosidade_logger.registrar_evento(evento)
import time

class MonitorOciosidade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MonitorOciosidade, cls).__new__(cls)
        return cls._instance

    def __init__(self, tempo_maximo_ocioso=10):
        if not hasattr(self, 'initialized'):
            self.tempo_maximo_ocioso = tempo_maximo_ocioso
            self.ultimo_evento = time.time()
            self.initialized = True

    def atualizar_ultimo_evento(self):
        self.ultimo_evento = time.time()

    def verificar_ociosidade(self):
        while True:
            tempo_atual = time.time()
            if tempo_atual - self.ultimo_evento > self.tempo_maximo_ocioso:
                print(f"O usuário está ocioso por mais de {self.tempo_maximo_ocioso} segundos.")
            time.sleep(1)
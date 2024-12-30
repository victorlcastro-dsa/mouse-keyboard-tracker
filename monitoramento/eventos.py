from pynput import keyboard, mouse
from threading import Thread
import time

class MonitorEventos:
    def __init__(self):
        self.teclado_eventos = []
        self.mouse_eventos = []
        self.ultimo_evento = time.time()
        self.observers = []

    def adicionar_observador(self, observador):
        self.observers.append(observador)

    def notificar_observadores(self):
        for observador in self.observers:
            observador.atualizar_ultimo_evento()

    def capturar_teclado(self):
        def on_press(key):
            self.teclado_eventos.append((time.time(), f"Tecla pressionada: {key}"))
            self.ultimo_evento = time.time()
            self.notificar_observadores()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def capturar_mouse(self):
        def on_click(x, y, button, pressed):
            evento = f"Mouse {'clicado' if pressed else 'solto'} em ({x}, {y}) com {button}"
            self.mouse_eventos.append((time.time(), evento))
            self.ultimo_evento = time.time()
            self.notificar_observadores()

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    def iniciar_monitoramento(self):
        Thread(target=self.capturar_teclado, daemon=True).start()
        Thread(target=self.capturar_mouse, daemon=True).start()
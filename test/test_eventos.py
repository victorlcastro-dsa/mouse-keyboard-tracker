import unittest
from monitoramento.eventos import MonitorEventos
import time

class TestMonitorEventos(unittest.TestCase):
    def setUp(self):
        self.monitor_eventos = MonitorEventos()

    def test_adicionar_observador(self):
        class MockObservador:
            def __init__(self):
                self.atualizado = False

            def atualizar_ultimo_evento(self):
                self.atualizado = True

        observador = MockObservador()
        self.monitor_eventos.adicionar_observador(observador)
        self.monitor_eventos.notificar_observadores()
        self.assertTrue(observador.atualizado)

    def test_capturar_teclado(self):
        self.monitor_eventos.teclado_eventos.append((time.time(), "Tecla pressionada: 'a'"))
        self.assertEqual(len(self.monitor_eventos.teclado_eventos), 1)

    def test_capturar_mouse(self):
        self.monitor_eventos.mouse_eventos.append((time.time(), "Mouse clicado em (100, 200) com Button.left"))
        self.assertEqual(len(self.monitor_eventos.mouse_eventos), 1)

if __name__ == '__main__':
    unittest.main()
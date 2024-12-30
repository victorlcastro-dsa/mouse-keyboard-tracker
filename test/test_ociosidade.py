import unittest
from monitoramento.ociosidade import MonitorOciosidade
import time

class TestMonitorOciosidade(unittest.TestCase):
    def setUp(self):
        self.monitor_ociosidade = MonitorOciosidade(tempo_maximo_ocioso=1)

    def test_atualizar_ultimo_evento(self):
        self.monitor_ociosidade.atualizar_ultimo_evento()
        self.assertAlmostEqual(self.monitor_ociosidade.ultimo_evento, time.time(), delta=1)

    def test_verificar_ociosidade(self):
        self.monitor_ociosidade.ultimo_evento = time.time() - 2
        with self.assertLogs(level='INFO') as log:
            self.monitor_ociosidade.verificar_ociosidade()
            self.assertIn('O usuário está ocioso por mais de 1 segundos.', log.output)

if __name__ == '__main__':
    unittest.main()
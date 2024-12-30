import unittest
from monitoramento.analise import AnaliseEventos

class TestAnaliseEventos(unittest.TestCase):
    def setUp(self):
        self.teclado_eventos = [(1620000000, "Tecla pressionada: 'a'")]
        self.mouse_eventos = [(1620000000, "Mouse clicado em (100, 200) com Button.left")]
        self.analise = AnaliseEventos(self.teclado_eventos, self.mouse_eventos)

    def test_gerar_relatorio(self):
        self.analise.gerar_relatorio()
        # Verifique se o relatório foi gerado corretamente (você pode usar mocks para capturar a saída)

if __name__ == '__main__':
    unittest.main()
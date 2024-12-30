import pandas as pd

class AnaliseEventos:
    def __init__(self, teclado_eventos, mouse_eventos):
        self.teclado_eventos = teclado_eventos
        self.mouse_eventos = mouse_eventos

    def gerar_relatorio(self):
        df_teclado = pd.DataFrame(self.teclado_eventos, columns=["Timestamp", "Evento"])
        df_mouse = pd.DataFrame(self.mouse_eventos, columns=["Timestamp", "Evento"])

        print("Relatório de Eventos do Teclado:")
        print(df_teclado.head())

        print("\nRelatório de Eventos do Mouse:")
        print(df_mouse.head())
from monitoramento.eventos import MonitorEventos
from monitoramento.ociosidade import MonitorOciosidade
from monitoramento.logger import EventoLogger
from threading import Thread
import time

def main():
    logger = EventoLogger.configurar_logger_principal()
    logger.info("Monitoramento iniciado.")

    monitor_eventos = MonitorEventos()
    monitor_ociosidade = MonitorOciosidade(tempo_maximo_ocioso=10)

    monitor_eventos.adicionar_observador(monitor_ociosidade)
    monitor_eventos.iniciar_monitoramento()

    Thread(target=monitor_ociosidade.verificar_ociosidade, daemon=True).start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logger.info("Monitoramento encerrado.")
        print("Monitoramento encerrado.")

if __name__ == "__main__":
    main()
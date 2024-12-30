from monitoramento.eventos import MonitorEventos
from monitoramento.ociosidade import MonitorOciosidade
from monitoramento.logger import EventoLogger
from monitoramento.log_manager import LogManager
from monitoramento.config import Config
from threading import Thread
import time
from datetime import datetime

def main():
    horario_inicio = datetime.now().strftime('%H-%M-%S')
    logger = EventoLogger.configurar_logger_principal()
    logger.info("Monitoramento iniciado.")

    monitor_eventos = MonitorEventos()
    monitor_ociosidade = MonitorOciosidade(tempo_maximo_ocioso=Config.TEMPO_MAXIMO_OCIOSO)

    monitor_eventos.adicionar_observador(monitor_ociosidade)
    monitor_eventos.iniciar_monitoramento()

    Thread(target=monitor_ociosidade.verificar_ociosidade, daemon=True).start()

    try:
        while True:
            time.sleep(Config.INTERVALO_SLEEP)
    except KeyboardInterrupt:
        logger.info("Monitoramento encerrado.")
        EventoLogger.fechar_loggers()
        LogManager.mover_logs_para_relatorios(horario_inicio)
        print("Monitoramento encerrado.")

if __name__ == "__main__":
    main()
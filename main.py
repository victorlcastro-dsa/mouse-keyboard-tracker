from monitoramento.eventos import MonitorEventos
from monitoramento.ociosidade import MonitorOciosidade
from monitoramento.logger import EventoLogger
from monitoramento.log_manager import LogManager
from monitoramento.config import Config
from threading import Thread
import time
from datetime import datetime

def configurar_monitoramento():
    """Configura e inicializa o monitoramento de eventos e ociosidade."""
    try:
        horario_inicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger = EventoLogger.configurar_logger_principal()
        logger.info("Monitoramento iniciado.")

        monitor_eventos = MonitorEventos()
        monitor_ociosidade = MonitorOciosidade(tempo_maximo_ocioso=Config.TEMPO_MAXIMO_OCIOSO)

        monitor_eventos.adicionar_observador(monitor_ociosidade)
        monitor_eventos.iniciar_monitoramento()

        Thread(target=monitor_ociosidade.verificar_ociosidade, daemon=True).start()

        return horario_inicio, logger, monitor_ociosidade
    except Exception as e:
        print(f"Erro ao configurar monitoramento: {e}")
        return None, None, None

def main():
    """Função principal que executa o monitoramento."""
    horario_inicio, logger, monitor_ociosidade = configurar_monitoramento()

    if not horario_inicio or not logger or not monitor_ociosidade:
        print("Falha ao iniciar o monitoramento.")
        return

    try:
        while True:
            time.sleep(Config.INTERVALO_SLEEP)
    except KeyboardInterrupt:
        try:
            logger.info("Monitoramento encerrado.")
            monitor_ociosidade.registrar_tempo_total_ociosidade()
            EventoLogger.fechar_loggers()
            LogManager.mover_logs_para_relatorios(horario_inicio)
            print("Monitoramento encerrado.")
        except Exception as e:
            print(f"Erro ao encerrar monitoramento: {e}")

if __name__ == "__main__":
    main()
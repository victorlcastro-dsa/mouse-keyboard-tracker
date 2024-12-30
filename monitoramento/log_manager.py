import os
import shutil
import time
from datetime import datetime
from monitoramento.config import Config

class LogManager:
    @staticmethod
    def verificar_ociosidade(horario_inicio):
        ociosidade_log_path = 'logs/ociosidade_eventos.log'
        if not os.path.exists(ociosidade_log_path) or os.path.getsize(ociosidade_log_path) == Config.TAMANHO_MINIMO_ARQUIVO:
            with open(ociosidade_log_path, 'a') as log_file:
                horario_fim = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_file.write(f'Não foram registrados períodos de inatividade entre {horario_inicio} e {horario_fim}.\n')

    @staticmethod
    def mover_logs_para_relatorios(horario_inicio):
        # Verifica e anota períodos de inatividade antes de mover os logs
        LogManager.verificar_ociosidade(horario_inicio)

        # Espera até que o arquivo ociosidade_eventos.log seja preenchido
        ociosidade_log_path = 'logs/ociosidade_eventos.log'
        while not os.path.exists(ociosidade_log_path) or os.path.getsize(ociosidade_log_path) == Config.TAMANHO_MINIMO_ARQUIVO:
            time.sleep(Config.INTERVALO_VERIFICACAO_ARQUIVO)  # Espera antes de verificar novamente

        timestamp = datetime.now().strftime('%Y-%m-%d')
        hora_atual = datetime.now().hour
        if Config.HORA_INICIO_MATUTINO <= hora_atual < Config.HORA_INICIO_VESPERTINO:
            periodo = 'matutino'
        elif Config.HORA_INICIO_VESPERTINO <= hora_atual < Config.HORA_INICIO_NOTURNO:
            periodo = 'vespertino'
        else:
            periodo = 'noturno'

        horario_inicio = horario_inicio.replace(':', '_')
        destino = f'relatorios/{timestamp}/{periodo}/{horario_inicio}'
        os.makedirs(destino, exist_ok=True)

        for arquivo in os.listdir('logs'):
            if arquivo.endswith('.log'):
                shutil.move(os.path.join('logs', arquivo), os.path.join(destino, arquivo))
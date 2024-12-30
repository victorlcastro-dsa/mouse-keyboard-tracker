import os
import shutil
from datetime import datetime
from monitoramento.config import Config

class LogManager:
    @staticmethod
    def mover_logs_para_relatorios(horario_inicio):
        timestamp = datetime.now().strftime('%Y-%m-%d')
        hora_atual = datetime.now().hour
        if Config.HORA_INICIO_MATUTINO <= hora_atual < Config.HORA_INICIO_VESPERTINO:
            periodo = 'matutino'
        elif Config.HORA_INICIO_VESPERTINO <= hora_atual < Config.HORA_INICIO_NOTURNO:
            periodo = 'vespertino'
        else:
            periodo = 'noturno'

        destino = f'relatorios/{timestamp}/{periodo}/{horario_inicio}'
        os.makedirs(destino, exist_ok=True)

        for arquivo in os.listdir('logs'):
            if arquivo.endswith('.log'):
                shutil.move(os.path.join('logs', arquivo), os.path.join(destino, arquivo))
class Config:
    TEMPO_MAXIMO_OCIOSO = 600  # Tempo máximo de ociosidade em segundos
    INTERVALO_CHECAGEM_OCIOSIDADE = 1  # Intervalo de checagem de ociosidade em segundos
    INTERVALO_SLEEP = 10  # Intervalo de sleep em segundos
    HORA_INICIO_MATUTINO = 6
    HORA_INICIO_VESPERTINO = 12
    HORA_INICIO_NOTURNO = 18
    TAMANHO_MINIMO_ARQUIVO = 0  # Tamanho mínimo do arquivo em bytes
    INTERVALO_VERIFICACAO_ARQUIVO = 1  # Intervalo de verificação do arquivo em segundos
    TEMPO_OCIOSO_ACUMULADO = 0  # Tempo ocioso acumulado inicial
    TEMPO_OCIOSO_TOTAL = 0  # Tempo ocioso total
    SEGUNDOS_EM_UM_MINUTO = 60  # Segundos em um minuto
    SEGUNDOS_EM_UMA_HORA = 3600  # Segundos em uma hora
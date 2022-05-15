import logging

def create_logger(nome_arquivo_log = 'logs.log'):
    file_handler = logging.FileHandler(f'log/{nome_arquivo_log}', 'a', 'utf-8')
    file_handler.setLevel(logging.WARNING)

    stream_handler = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[stream_handler, file_handler])

def debug(msg):
    logging.debug(msg)
def info(msg):
    logging.info(msg)
def warning(msg):
    logging.warning(msg)
def error(msg):
    logging.error(msg)
def critical(msg):
    logging.critical(msg)
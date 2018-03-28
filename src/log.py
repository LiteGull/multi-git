import logging


def logger_setup():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging_handler(logger)
    return logger


def logging_handler(logger):
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', '%H:%M:%S')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

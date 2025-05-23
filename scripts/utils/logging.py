import sys
import logging

def setup_logger(name, level=logging.DEBUG):
    formatter = logging.Formatter (fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                   datefmt='%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler (sys.stdout)
    console_handler.setFormatter(formatter)

    # File Handler
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    return logger

logger = setup_logger(name='sample')

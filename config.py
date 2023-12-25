import logging
import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_DATA_DIR = "static_data"




def configure_logger(name: str, level=logging.INFO):
    """
    Configures and returns a logger with the given name and level.

    :param name: Name of the logger.
    :param level: Logging level, e.g., logging.INFO, logging.DEBUG.
    :return: Configured logger.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers (e.g., console handler, file handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)

    return logger

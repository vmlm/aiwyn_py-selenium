import logging


def configure_logger(context):
    # Configure logging programmatically
    logger = logging.getLogger('behave')
    logger.setLevel(logging.INFO)

    # Create file handler for logging to a file
    file_handler = logging.FileHandler(f"{context.results_dir}/actions.log")
    file_handler.setLevel(logging.INFO)

    # Create a formatter and set it
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)

    return logger


def set_logger_level_error(logger):
    logging.getLogger(logger).setLevel(logging.ERROR)


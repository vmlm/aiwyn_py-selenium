import logging


def configure_behave_logger(context):
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


def configure_additional_loggers(context):
    # Set the WDM logger level to ERROR, so we don't get webdriver configuration messages
    logging.getLogger('WDM').setLevel(logging.ERROR)


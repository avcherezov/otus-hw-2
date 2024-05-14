import logging


class Logger:
    logger = logging.getLogger('server_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('log.log')
    handler.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter('%(asctime)s - %(name)s'
                                      ' - %(levelname)-8s - %(message)s')
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)

    @classmethod
    def log(cls, msg):
        cls.logger.info(msg=msg)

import logging
import inspect

class LogGen:
    def Loggen(logLevel=logging.DEBUG):
        logger_name= inspect.stack()[1] [3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation1.log")
        logger.addHandler(fh)
        return logger
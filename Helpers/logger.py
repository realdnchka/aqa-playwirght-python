import logging
from configuration import Configuration


class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self
            self.logger = logging.getLogger("AT")
            if Configuration().logging == 'true':
                self.logger.setLevel(logging.INFO)
                fh = logging.FileHandler('tests.log')
                fh.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)

    # TODO make fabric for loggers, ex: API and UI

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
        Logger.__instance = self
        self.logger = logging.getLogger("AT")
        if Configuration().logging == 'true':
            self.logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler('tests.log')
            file_handler.setLevel(logging.INFO)
            formatter = \
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def clear_logs(self):
        with open('tests.log', 'r+') as file:
            file.truncate(0)
    # TODO make fabric for loggers, ex: API and UI

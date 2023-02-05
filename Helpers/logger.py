import logging
from configuration import Configuration


class Logger:
    def __int__(self, name):
        self.logger = logging.getLogger(name)
        if Configuration().logging == 'true':
            self.logger.setLevel(logging.INFO)
            fh = logging.FileHandler('tests.log')
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

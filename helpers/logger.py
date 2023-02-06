import logging
import os

from configuration import Configuration
import shutil
import datetime


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("")
        self.src = 'last_test.log'

    def create_logger(self, name):
        if Configuration().logging == 'true':
            self.logger = logging.getLogger(name)
            if self.logger.hasHandlers():
                self.logger.handlers.clear()
            self.logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler('last_test.log')
            file_handler.setLevel(logging.INFO)
            formatter = \
                logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def copy_last_logs(self):
        src = self.src
        dst = f'logs/{str(datetime.datetime.now())}.log'
        shutil.copy(src, dst)

    def clear_logs(self):
        with open(self.src, 'r+') as file:
            file.truncate(0)

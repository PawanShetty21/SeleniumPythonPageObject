import logging
import time


class Logger():

# Creating constructor to call logger object
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # Create file handler
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        # To store logfile inside Logs folder
        curr_time = time.strftimeg("%Y-%m-%d")
        self.LogFileName = '../Logs/log' + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="w")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
import logging
import time
import traceback


class Logger:

    def __init__(self, logger, file_level=logging.INFO):
        try:
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
            curr_date = time.strftime("%Y-%m-%d-%H-%M-%S")
            self.LogFileName = '../Logs/log_' + curr_date + '.txt'
            # "a" to append the logs in same file, "w" to generate new logs and delete old one
            fh = logging.FileHandler(self.LogFileName, mode="a")
            fh.setFormatter(fmt)
            fh.setLevel(file_level)
            self.logger.addHandler(fh)
        except:
            print(traceback.print_exc())

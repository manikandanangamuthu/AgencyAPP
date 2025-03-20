import logging

class LogGen:

    @staticmethod

    def loggen():
        logging.basicConfig(filename="C://Users//05444//PycharmProjects//AgencyApp//Logs//automation.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
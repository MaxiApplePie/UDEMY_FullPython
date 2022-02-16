import logging

logging.basicConfig(level=logging.ERROR,
        filename='S48_LOGGING/app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Debug")
logging.info("Info")
logging.warning("C'est un warning !")
logging.error('Error')
logging.critical('Critical')
import logging
import os
import pytest
# logging.basicConfig(filename="test3.log",
#                         format='%(asctime)s: %(levelname)s: %(message)s',
#                         datefmt='%m/%d/%Y %I:%M:%S %p',
#                         level=logging.DEBUG
#                         )
logging.basicConfig(filename="test4.log", level=logging.INFO)
logging.info('start')
pytest.main()
logging.info('done')
logger = logging.getLogger()

def test():

    #logger.setLevel(logging.DEBUG)  # it sets debug as the basic level of log otherwise
    # if debug would not be given the basic level will be warning

    #logging.debug("this is a debug message ")
    logger.info("This is debug message ")
    assert '23==23',"message"
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")

if __name__ == '__main__':
 logger.info(' About to start the tests ')
 logger.main(args=[os.path.abspath("test3.log")])
 logger.info(' Done executing the tests ')
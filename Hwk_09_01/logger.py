
import logging

logging.basicConfig(
    level=logging.INFO, filename='Homework\Hwk_09_01\loglist.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',)
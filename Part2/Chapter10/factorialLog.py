#!/bin/python

import logging
# logging.disable(logging.CRITICAL)
logging.basicConfig(filename = 'myProgramLog',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' %(n))

    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of fauctorial(%s%%)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')


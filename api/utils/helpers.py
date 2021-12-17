import random

def randomizer():
    ''''
        returns 7 random character
    '''
    rndm = ''.join(random.sample('0123456789qwertyuiopasdfghjklzxcvbnm', 7))
    return rndm
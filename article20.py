from datetime import datetime
from time import sleep

def log(message, when=datetime.now()):
    print('%s: %s' %(when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')



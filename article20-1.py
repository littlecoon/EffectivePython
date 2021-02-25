from datetime import datetime
from time import sleep

def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message:Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')

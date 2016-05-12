#!/Users/kawasakitaku/Documents/python-PVM/ln-python2.7/bin/python2.7

import sys
from twisted.python import log
from log_colorizer import ColorizedLogObserver

observer = ColorizedLogObserver(sys.stdout)
log.addObserver(observer.emit)

log.msg("Starting Experiment")
log.msg("Logging an exception")

try:
    1 / 0
except ZeroDivisionError as e:
    log.err(e)

log.msg("Ending experiment")

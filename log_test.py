#!/Users/kawasakitaku/Documents/python-PVM/ln-python2.7/bin/python2.7

import sys
from twisted.python import log

log.startLogging(sys.stdout)
log.msg("Starting experiment")

log.msg("Logging an exception")

try:
    1/0
except ZeroDivisionError as e:
    log.err(e)

log.msg("Ending expriment")


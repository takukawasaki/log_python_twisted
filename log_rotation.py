#!/Users/kawasakitaku/Documents/python-PVM/ln-python2.7/bin/python2.7

from twisted.python import log
from twisted.python import logfile

f = logfile.LogFile("test.log","/tmp",rotateLength=100)
log.startLogging(f)

log.msg("First Message")

f.rotate()
for i in range(5):
    log.msg("Test message",i)

log.msg("Last message")


"""logging configuration support"""

# System imports
import logging.handlers
import sys


#: logging formatters
_formatters = {
    'msgonly': {
        'format': '%(message)s'
    },
    'minimal': {
        'format': '(%(name)s) %(message)s'
    },
    'normal': {
        'format': '%(asctime)s (%(name)s) %(levelname)s %(message)s'
    },
    'debug': {
        'format': '%(asctime)s (%(name)s) %(levelname)s %(module)s %(funcName)s %(message)s'
    }
}

#: logging stream handler string
LOGGING_STREAM_HANDLER = 'logging.StreamHandler'
#: logging timed file handler string
LOGGING_TIMED_FILE_HANDLER = 'logging.handlers.TimedRotatingFileHandler'

#: logging handlers
_handlers = {
    'debugHandler': {
        'class': LOGGING_STREAM_HANDLER,
        'level': logging.DEBUG,
        'formatter': 'debug',
        'stream': sys.stdout,
    },
    'consoleHandler': {
        'class': LOGGING_STREAM_HANDLER,
        'level': logging.DEBUG,
        'formatter': 'normal',
        'stream': sys.stdout,
    },
    'fileHandler': {
        'class': LOGGING_TIMED_FILE_HANDLER,
        'level': logging.DEBUG,
        'formatter': 'normal',
        'filename': 'logging.log',
        'when': 'D',
        'interval': 1,
        'backupCount': 7,
        'delay': True,
    },
}

#: Loggers
_loggers = {
    '': {
        'level': logging.INFO,
        'handlers': ['consoleHandler', 'fileHandler'],
        'qualname': 'root',
        'propagate': False,
    },
    'root': {
        'level': logging.DEBUG,
        'handlers': ['debugHandler', 'fileHandler'],
        'qualname': 'root',
        'propagate': False,
    },
    '__main__': {
        'level': logging.DEBUG,
        'handlers': ['debugHandler', 'fileHandler'],
        'qualname': '__main__',
        'propagate': False,
    },
    'main': {
        'level': logging.DEBUG,
        'handlers': ['debugHandler', 'fileHandler'],
        'qualname': 'main',
        'propagate': False,
    },
}

#: Configuration dictionary
LOGGING = {
    "version": 1,
    "loggers": _loggers,
    "handlers": _handlers,
    "formatters": _formatters,
}

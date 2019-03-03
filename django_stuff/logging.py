import logging
import warnings


warnings.simplefilter('default')


def get_loggers(level, loggers):
    logging.addLevelName('DISABLED', logging.CRITICAL + 10)

    log_config = {
        'handlers': ['console'],
        'level': level,
    }

    if level == 'DISABLED':
        loggers = {'': {'handlers': ['null'], 'level': 'DEBUG', 'propagate': False}}
    else:
        loggers = {logger.strip(): log_config for logger in loggers}

    loggers.update({
        'parso': {
            'propagate': False,
        }
    })

    return loggers


def get_logging_config(loggers=None):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)s %(message)s'},
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'null': {
                'class': 'logging.NullHandler',
            },
        },
        'loggers': loggers or {},
    }

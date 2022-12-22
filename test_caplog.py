
class TestCapLog:

    def _test_logger(self, tf_caplog):
        # display capture log
        print("\nCAPLOG:")
        output = tf_caplog.text.rstrip('\n').split(sep='\n')
        if output == ['']:
            print("Nothing captured")
        else:
            for i in range(len(output)):
                print(f'{i}: {output[i]}')

    def test_caplog0_root(self, caplog):
        """Test caplog 'root' logger w/o dictConfig()"""
        import logging
        # use logging configuration "as-is"
        logger = logging.getLogger()
        # log at all logging levels
        logger.debug('DEBUG: log entry captured')
        logger.info('INFO: log entry captured')
        logger.error('ERROR: log entry captured')
        logger.warning('WARNING: log entry captured')
        self._test_logger(caplog)

    def test_caplog1_main1(self, caplog):
        """Test caplog 'main' logger w/ dictConfig(), propagate=False"""
        import logging.config
        import logging
        import log_config
        # configure logging, propagate False
        log_config.LOGGING['loggers']['main']['propagate'] = False
        logging.config.dictConfig(log_config.LOGGING)
        logger = logging.getLogger(name='main')
        # log at all logging levels
        logger.debug('DEBUG: log entry captured')
        logger.info('INFO: log entry captured')
        logger.error('ERROR: log entry captured')
        logger.warning('WARNING: log entry captured')
        self._test_logger(caplog)

    def test_caplog1_main2(self, caplog):
        """Test caplog 'main' logger w/ dictConfig(), propagate=True"""
        import logging.config
        import logging
        import log_config
        # configure logging, propagate True
        log_config.LOGGING['loggers']['main']['propagate'] = True
        logging.config.dictConfig(log_config.LOGGING)
        logger = logging.getLogger(name='main')
        # log at all logging levels
        logger.debug('DEBUG: log entry captured')
        logger.info('INFO: log entry captured')
        logger.error('ERROR: log entry captured')
        logger.warning('WARNING: log entry captured')
        self._test_logger(caplog)

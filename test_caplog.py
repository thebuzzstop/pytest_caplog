def _test_logger(logger, tf_caplog) -> bool:
    """Display caplog capture text"""
    # log at all logging levels
    logger.debug('DEBUG: log entry captured')
    logger.info('INFO: log entry captured')
    logger.error('ERROR: log entry captured')
    logger.warning('WARNING: log entry captured')
    # display capture log
    print("\nCAPLOG:")
    output = tf_caplog.text.rstrip('\n').split(sep='\n')
    if output == ['']:
        print("Nothing captured")
        return False
    for i in range(len(output)):
        print(f'{i}: {output[i]}')
    return True


class TestCapLog:

    def test_caplog0_root(self, caplog):
        """Test caplog 'root' logger w/o dictConfig()"""
        import logging
        # use logging configuration "as-is"
        logger = logging.getLogger()
        assert _test_logger(logger, caplog)

    def test_caplog1_main1(self, caplog):
        """Test caplog 'main' logger w/ dictConfig(), propagate=False"""
        import logging.config
        import logging
        import log_config
        # configure logging, propagate False
        log_config.LOGGING['loggers']['main']['propagate'] = False
        logging.config.dictConfig(log_config.LOGGING)
        logger = logging.getLogger(name='main')
        assert _test_logger(logger, caplog)

    def test_caplog1_main2(self, caplog):
        """Test caplog 'main' logger w/ dictConfig(), propagate=True"""
        import logging.config
        import logging
        import log_config
        # configure logging, propagate True
        log_config.LOGGING['loggers']['main']['propagate'] = True
        logging.config.dictConfig(log_config.LOGGING)
        logger = logging.getLogger(name='main')
        assert _test_logger(logger, caplog)

    def test_caplog1_add_caplog_handlers(self, caplog):
        """Test caplog 'main' logger w/ dictConfig(), propagate=True"""
        import logging.config
        import logging
        import log_config
        # configure logging, propagate True
        log_config.LOGGING['loggers']['main']['propagate'] = True
        logging.config.dictConfig(log_config.LOGGING)
        logger = logging.getLogger(name='main')
        logger.addHandler(hdlr=caplog.handler)
        caplog.handler.level = logger.level
        assert _test_logger(logger, caplog)

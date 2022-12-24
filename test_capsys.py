def _test_output(tf_capsys) -> bool:
    """Display capsys capture text"""
    # display capture output
    print("\nCAPSYS:")
    output = tf_capsys.readouterr()
    capsys_out = (output.out.rstrip('\n')).split(sep='\n')
    capsys_err = (output.err.rstrip('\n')).split(sep='\n')
    if capsys_err != ['']:
        return False
    if capsys_out == ['']:
        print("Nothing captured")
        return False
    for i in range(len(capsys_out)):
        print(f'{i}: {capsys_out[i]}')
    return True


class TestCapSys:

    def test_capsys0_root(self, capsys):
        """Test capsys using 'root' logger w/o dictConfig()"""
        import logging
        # use logging configuration "as-is"
        logger = logging.getLogger()
        # log at all logging levels
        logger.debug('DEBUG: log entry captured')
        logger.info('INFO: log entry captured')
        logger.error('ERROR: log entry captured')
        logger.warning('WARNING: log entry captured')
        with capsys.disabled():
            assert _test_output(tf_capsys=capsys)

    def test_capsys1_main1(self, capsys):
        """Test capsys using 'main' logger w/ dictConfig(), propagate=False"""
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
        with capsys.disabled():
            assert _test_output(capsys)

    def test_capsys1_main2(self, capsys):
        """Test capsys using 'main' logger w/ dictConfig(), propagate=True"""
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
        with capsys.disabled():
            assert _test_output(capsys)

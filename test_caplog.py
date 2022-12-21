
class TestCapLog:

    def logging(self, logger, tf_caplog):
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
        else:
            for i in range(len(output)):
                print(f'{i}: {output[i]}')

    def test_caplog0_root(self, caplog):
        import logging
        # use logging configuration "as-is"
        self.logging(logging.getLogger(), caplog)

    def test_caplog1_main(self, caplog):
        import logging.config
        import logging
        import log_config
        # configure logging
        logging.config.dictConfig(log_config.LOGGING)
        self.logging(logging.getLogger(name='main'), caplog)


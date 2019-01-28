import logging
import os.path as osp
import time


def get_time_str():
    return time.strftime('%Y%m%d_%H%M%S', time.localtime())


def get_root_logger(log_level=logging.INFO):
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=log_level)
    return logger


def init_logger(log_dir=None, level=logging.INFO):
    """Init the logger.

    Args:
        log_dir(str, optional): Log file directory. If not specified, no
            log file will be used.
        level (int or str): See the built-in python logging module.

    Returns:
        :obj:`~logging.Logger`: Python logger.
    """
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=level)
    logger = logging.getLogger(__name__)
    if log_dir:
        filename = '{}.log'.format(get_time_str())
        log_file = osp.join(log_dir, filename)
        _add_file_handler(logger, log_file, level=level)
    return logger


def _add_file_handler(logger,
                      filename=None,
                      mode='w',
                      level=logging.INFO):
    # TODO: move this method out of runner
    file_handler = logging.FileHandler(filename, mode)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    return logger


logger = init_logger('./')

for i in range(100):
    logger.info('iter {}'.format(i))

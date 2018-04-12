import logging

logger = logging.getLogger('monitor-rabbitmq')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor-rabbitmq.log')
sh = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

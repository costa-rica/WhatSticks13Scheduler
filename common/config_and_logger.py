import os
from ws_config import ConfigWorkstation, ConfigDev, ConfigProd
import logging
from logging.handlers import RotatingFileHandler

match os.environ.get('WS_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- WhatSticks13Scheduler/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- WhatSticks13Scheduler/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- WhatSticks13Scheduler/config: Local')

#Setting up Logger
app_name = "WS11Scheduler"
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter = logging.Formatter(f'%(asctime)s - {app_name} - %(name)s - [%(filename)s:%(lineno)d] - %(message)s')

#initialize a logger
logger_scheduler = logging.getLogger(__name__)
logger_scheduler.setLevel(logging.DEBUG)

#where do we store logging information
file_handler = RotatingFileHandler(os.path.join(config.SCHEDULER_SERVICE_11_ROOT,'scheduler_service.log'), mode='a', maxBytes=5*1024*1024,backupCount=2)
file_handler.setFormatter(formatter)

#where the stream_handler will print
stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter_terminal)
stream_handler.setFormatter(formatter)

logger_scheduler.addHandler(file_handler)
logger_scheduler.addHandler(stream_handler)

import logging

# configure logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# create a logger instance
logger = logging.getLogger(__name__)
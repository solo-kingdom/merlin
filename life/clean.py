# coding: utf-8
import os

from common import logger
from constants.constants import PATH_MERLIN


def clean(context):
    if os.getenv("HOME") != os.getcwd():
        cmd = 'rm -r %s/*' % PATH_MERLIN
        logger.info('clean done. [cmd=%s, result=%s]', cmd, os.system(cmd) == 0)

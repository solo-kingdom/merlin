# coding: utf-8
from common.common import logger
from life.life import config, STAGE_PACKAGE


def build(args):
    logger.info('arg: %s, config: %s', args, config(STAGE_PACKAGE))

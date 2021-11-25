# coding: utf-8
from common.common import logger
from life.life import config, STAGE_DEPLOY


def deploy(args):
    logger.info('arg: %s, config: %s', args, config(STAGE_DEPLOY))

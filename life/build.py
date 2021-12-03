# coding: utf-8
from common import logger
from life.life import config, STAGE_BUILD


def build(args):
    logger.info('arg: %s, config: %s', args, config(STAGE_BUILD))

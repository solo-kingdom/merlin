# coding: utf-8
from common.common import logger
from constants.constants import *
from life.package.sample import pack as sample_pack
from model.context import Context


def pack(context: Context):
    logger.debug('package process. [modules=%s]', context.config.modules())
    for module in context.config.modules().items():
        logger.debug('package module. [module=%s, config=%s]', module[0], module[1])
        if TYPE_SAMPLE == module[1][K_TYPE]:
            sample_pack(context, module[0], module[1])

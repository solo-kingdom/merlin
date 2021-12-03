# coding: utf-8
import json

from common import logger
from common.file import ensure_path
from constants.constants import *
from life.package.pack import PackConfig, TarPack, NoPack
from model.context import Context


def pack(context: Context):
    logger.debug('package process. [modules=%s]', context.config.modules())
    ensure_path(PATH_MERLIN)

    for module in context.config.modules().items():
        logger.debug('package module. [module=%s, config=%s]', module[0], module[1])
        pc = PackConfig(module[0], **module[1][STAGE_PACKAGE])
        tp = module[1][K_TYPE]
        if TYPE_SAMPLE == tp:
            TarPack(context, pc).do()
        elif TYPE_NO_PACK == tp:
            NoPack(context, pc).do()
        else:
            logger.error('unknown package type. [type=%s]', tp)
    logger.debug('package done. [packaged=%s]', json.dumps(context.pack.packages, default=vars))

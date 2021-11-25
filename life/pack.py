# coding: utf-8

from life.life import config, STAGE_PACKAGE, K_TYPE, K_MODULE
from life.package.sample import pack as sample_pack

TYPE_SAMPLE = 'sample'


def pack(args):
    cfg = config(STAGE_PACKAGE)
    for module in cfg:
        tp = module[K_TYPE]
        if TYPE_SAMPLE == tp:
            sample_pack(module[K_MODULE], module[STAGE_PACKAGE])

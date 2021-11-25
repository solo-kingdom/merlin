# coding: utf-8
import os

from common.common import logger
from common.common.file import ensure_path

K_BASE = 'base'
K_EXCLUDE = 'exclude'
PATH_MERLIN = '.merlin'


def pack(module, cfg):
    base = cfg[K_BASE] if cfg[K_BASE] else module
    ensure_path(PATH_MERLIN)
    exclude = cfg[K_EXCLUDE] if cfg[K_EXCLUDE] else []
    fls = os.listdir(base)
    fls = list(filter(lambda x: not x.startswith('.') and x not in exclude, fls))
    logger.info('files=%s', fls)
    include = (' ' + base + '/').join(fls)
    cmd = 'tar -czf %s/%s.tar.gz %s' % (PATH_MERLIN, module, include)
    logger.info('cmd=[%s]', cmd)
    assert os.system(cmd) == 0, 'package module %s failed. [config=%s]' % (module, str(cfg))
    logger.info('package module success. [module=%s, target=%s/%s.tar.gz]', module, PATH_MERLIN, module)

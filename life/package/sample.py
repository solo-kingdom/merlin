# coding: utf-8
import os

from common.common import logger
from common.common.file import ensure_path

K_BASE = 'base'
K_EXCLUDE = 'exclude'
PATH_MERLIN = '.merlin'


def pack(module, cfg):
    logger.info('config: %s', cfg)
    base = cfg[K_BASE] if cfg[K_BASE] else module
    ensure_path(PATH_MERLIN)
    exclude = ' '.join(['--exclude="' + i + '"' for i in cfg[K_EXCLUDE]]) if cfg[K_EXCLUDE] else ''
    cmd = 'tar -cf %s.tar %s --exclude=".?*" %s -C %s' % (module, base, exclude, PATH_MERLIN)
    logger.info('cmd=[%s]', cmd)
    assert os.system(cmd) == 0, 'package module %s failed. [config=%s]' % (module, str(cfg))

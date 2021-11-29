# coding: utf-8
import os

from common.common import logger
from constants.constants import PATH_MERLIN
from model.context import Context


class PackConfig:
    def __init__(self, module: str, base: str = '.', dest: str = '',
                 includes: list[str] = None, excludes: list[str] = None, *args, **kwargs):
        self.module = module
        self.base: str = base
        self.includes: list[str] = includes if includes is not None else []
        self.excludes: list[str] = excludes if excludes is not None else []


class TarPack:
    def __init__(self, context: Context, config: PackConfig):
        self.config = config
        self.context = context

    def do(self):
        module = self.config.module
        fls = os.listdir(self.config.base)
        # TODO regex match
        fls = list(filter(lambda x: not x.startswith('.') and x not in self.config.excludes, fls))
        logger.info('files=%s', fls)
        include = (' ' + self.config.base + '/').join(fls)

        target = '%s/%s.tar.gz' % (PATH_MERLIN, module)
        cmd = 'tar -czf %s %s' % (target, include)
        logger.info('cmd=[%s]', cmd)
        assert os.system(cmd) == 0, 'package module %s failed. [config=%s]' % (module, str(self.config))
        logger.info('package module success. [module=%s, target=%s]', module, target)
        self.context.pack.add(module, target)


class NonPack:
    def __init__(self, context: Context, config: PackConfig):
        self.config = config
        self.context = context

    def do(self):
        # TODO need to complete
        pass

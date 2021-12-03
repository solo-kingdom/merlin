# coding: utf-8
import os

from common import logger
from constants.constants import PATH_MERLIN
from model.context import Context


class PackConfig:
    def __init__(self, module: str, base: str = '.', dest: str = '',
                 includes=None, excludes=None, *args, **kwargs):
        self.module = module
        self.base: str = base
        self.includes: list[str] = includes if includes is not None else []
        self.excludes: list[str] = excludes if excludes is not None else []
        logger.debug('construct pack config. [module=%s, base=%s, includes=%s, excludes=%s]',
                     module, base, includes, excludes)


class PackUtils:
    @classmethod
    def retrieve_path(cls, config, f):
        return str(os.path.join(config.base, f))

    @classmethod
    def list_files(cls, config) -> list:
        if config.includes:
            fls = config.includes
        else:
            fls = os.listdir(config.base)
            # TODO regex match
            fls = list(filter(lambda x: not x.startswith('.') and x not in config.excludes, fls))

        fls = [cls.retrieve_path(config, i) for i in fls]
        logger.debug('files to pack. [files=%s]', fls)
        return fls


class Pack:
    def __init__(self, context: Context, config: PackConfig):
        self.config = config
        self.context = context

    def record(self, module, file):
        self.context.pack.add(module, file)


class TarPack(Pack):
    def __init__(self, context: Context, config: PackConfig):
        super().__init__(context, config)

    def do(self):
        module = self.config.module
        includes = ' '.join(PackUtils.list_files(self.config))
        target = '%s/%s.tar.gz' % (PATH_MERLIN, module)
        excludes = ' '.join(['--exclude ' + i for i in self.config.excludes])
        cmd = 'tar -czf %s %s %s' % (target, excludes, includes)
        logger.debug('pack command. [cmd=%s]', cmd)
        assert os.system(cmd) == 0, 'package module %s failed. [config=%s]' % (module, str(self.config))
        logger.info('package module success. [module=%s, target=%s]', module, target)
        self.record(module, target)


class NoPack(Pack):
    def __init__(self, context: Context, config: PackConfig):
        super().__init__(context, config)

    def do(self):
        assert len(self.config.includes) == 1, \
            'no pack type module must set one item in includes. [current=%s]' % self.config.includes

        include = self.config.includes[0]
        cmd = 'cp -r %s %s' % (PackUtils.retrieve_path(self.config, include), PATH_MERLIN)
        logger.debug('copy target. [cmd=%s]', cmd)
        assert os.system(cmd) == 0, 'copy target failed. [fail=%s]' % include
        self.record(self.config.module, os.path.join(PATH_MERLIN, include))

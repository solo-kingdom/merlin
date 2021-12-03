# coding: utf-8
import json
import os
from datetime import datetime

from common import logger
from constants.constants import *

F_PACKAGE = 'package.json'
F_PUBLISH = 'publish.json'


class Context:
    def __init__(self, args, config):
        self.args = args
        self.config = Config(config)
        self.start = datetime.now()
        self.pack = PackContext(config)
        self.publish = PublishContext()

    def finish(self):
        self.pack.finish(self.start)
        self.publish.finish(self.start)

    def load(self):
        self.pack.load()


class Packaged:
    def __init__(self, module, file):
        self.module = module
        self.file = file

    def to_dict(self):
        return {
            'module': self.module,
            'file': self.file
        }

    def __str__(self):
        return json.dumps(self.to_dict())


class PackContext:
    def __init__(self, config):
        self.packages: list[Packaged] = []
        self.info = Info(config[K_INFO])

    def add(self, module, file):
        self.packages.append(Packaged(module, file))

    def finish(self, start):
        if self.packages:
            data = {
                K_START: str(start),
                K_END: str(datetime.now()),
                K_INFO: self.info.to_dict(),
                K_PACKAGES: [i.to_dict() for i in self.packages]
            }
            with open(self.output(), 'w') as f:
                json.dump(data, f, indent=4)

    def load(self):
        with open(self.output(), 'r') as f:
            data = json.load(f)
            self.info = Info(data[K_INFO])
            self.packages = []
            for package in data[K_PACKAGES]:
                self.add(**package)
            logger.debug('load pack context. [info=%s, packages=%s]',
                         self.info, self.packages)

    def output(self):
        return os.path.join(PATH_MERLIN, F_PACKAGE)


class PublishContext:
    def finish(self, start):
        pass


class Config:
    def __init__(self, config):
        self.config = config
        self.info = Info(config[K_INFO])

    def modules(self):
        return self.config.get(K_MODULES, [])

    def module(self, module):
        return self.config.get(K_MODULES, )


class Info:
    def __init__(self, info):
        self.space = info[K_SPACE]
        self.product = info[K_PRODUCT]
        self.version = info[K_VERSION]

    def to_dict(self):
        return {
            'space': self.space,
            'product': self.product,
            'version': self.version
        }

    def __str__(self):
        return json.dumps(self.to_dict())

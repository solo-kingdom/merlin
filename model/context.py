# coding: utf-8
from datetime import datetime

from constants.constants import *


class Context:
    def __init__(self, args, config):
        self.args = args
        self.config = Config(config)
        self.start = datetime.now()
        self.pack = PackContext()
        self.publish = PublishContext()


class Packaged:
    def __init__(self, module, file):
        self.module = module
        self.file = file


class PackContext:
    def __init__(self):
        self.packages: list[Packaged] = []

    def add(self, module, file):
        self.packages.append(Packaged(module, file))


class PublishContext:
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

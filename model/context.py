# coding: utf-8
from datetime import datetime

from constants.constants import K_MODULES


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

    def modules(self):
        return self.config.get(K_MODULES, [])

    def module(self, module):
        return self.config.get(K_MODULES, )

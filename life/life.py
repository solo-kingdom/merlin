# coding: utf-8
import os

import yaml

from common import logger
from constants.constants import *


def check(args, stage=None):
    assert os.path.exists(PATH_PACKAGE), 'config file package.yml not exists'
    with open(PATH_PACKAGE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        inf = data.get('info', {})
        for item in inf.items():
            logger.info('%s: %s', *item)


def info():
    assert os.path.exists(PATH_PACKAGE), 'config file package.yml not exists'
    with open(PATH_PACKAGE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data.get('info', {})


def config():
    assert os.path.exists(PATH_PACKAGE), 'config file package.yml not exists'
    with open(PATH_PACKAGE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

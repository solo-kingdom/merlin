# coding: utf-8
import os

import yaml

from common.common import logger

PATH_PACKAGE = 'life/life.yml'
K_MODULES = 'modules'
K_MODULE = 'module'
K_TYPE = 'type'
STAGE_BUILD = 'build'
STAGE_PACKAGE = 'package'
STAGE_DEPLOY = 'deploy'


def check(args, stage=None):
    assert os.path.exists(PATH_PACKAGE), 'config file package.yml not exists'
    with open(PATH_PACKAGE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        logger.info(data)
        info = data.get('info', {})
        for item in info.items():
            logger.info('%s: %s', *item)


def config(stage=None):
    assert os.path.exists(PATH_PACKAGE), 'config file package.yml not exists'
    with open(PATH_PACKAGE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        modules = data.get(K_MODULES, [])
        return list(map(lambda md: {
            K_MODULE: md[0],
            stage: md[1].get(stage, {}),
            K_TYPE: md[1][K_TYPE]
        }, modules.items()))

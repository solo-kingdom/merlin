# coding: utf-8
import os

from common.common import logger
from common.common.request.file import upload
from constants.constants import *


def publish(context):
    logger.debug('publish. [arg=%s, config=%s]', context.args, context.config)
    cfg = context.config
    space = cfg[K_INFO][K_SPACE]
    product = cfg[K_INFO][K_PRODUCT]
    version = cfg[K_INFO][K_VERSION]
    modules = cfg[K_MODULES]
    for module in modules.items():
        name = module[0]
        f = os.path.join(PATH_MERLIN, '%s.tar.gz' % name)
        info = name, space, product, version, f
        logger.info('prepare to upload package. [name=%s, space=%s, product=%s, version=%s, file=%s]', *info)
        # TODO replace with product uploading url
        assert upload('http://127.0.0.1:8088/api/v1/package', {
            'space': space,
            'product': product,
            'version': version
        }, {}, f), 'upload package failed. [name=%s, space=%s, product=%s, version=%s, file=%s]' % info
        logger.info('upload packaged success. [name=%s, space=%s, product=%s, version=%s, file=%s]', *info)

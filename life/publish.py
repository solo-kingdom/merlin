# coding: utf-8
import os

from common.common import logger
from common.common.request.file import upload
from constants.constants import *
from model.context import Context


def publish(context: Context):
    logger.debug('publish. [arg=%s, config=%s]', context.args, cfg)

    for module in context.config.modules().items():
        name = module[0]
        f = os.path.join(PATH_MERLIN, '%s.tar.gz' % name)
        info = name, ci.space, ci.product, ci.version, f
        logger.info('prepare to upload package. [name=%s, space=%s, product=%s, version=%s, file=%s]', *info)
        # TODO replace with product uploading url
        assert upload('http://127.0.0.1:8088/api/v1/package', {
            'space': ci.space,
            'product': ci.product,
            'version': ci.version
        }, {}, f), 'upload package failed. [name=%s, space=%s, product=%s, version=%s, file=%s]' % info
        logger.info('upload packaged success. [name=%s, space=%s, product=%s, version=%s, file=%s]', *info)

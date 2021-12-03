# coding: utf-8
import json

from common import logger
from common.request.file import upload
from model.context import Context


def publish(context: Context):
    context.load()
    logger.debug('publish. [arg=%s, info=%s, packages=%s]',
                 context.args, context.pack.info, json.dumps(context.pack.packages, default=vars))
    ci = context.pack.info

    for module in context.pack.packages:
        info = module.module, ci.space, ci.product, module.module, ci.version, module.file
        logger.info('prepare to upload package. [name=%s, space=%s, product=%s, '
                    'module=%s, version=%s, file=%s]', *info)
        assert upload('http://eubalaena.srv.wii.pub/api/v1/package', {
            'space': ci.space,
            'product': ci.product,
            'module': module.module,
            'version': ci.version
        }, {}, module.file), \
            'upload package failed. [name=%s, space=%s, product=%s, module=%s, version=%s, file=%s]' % info
        logger.info('upload packaged success. [name=%s, space=%s, product=%s, '
                    'module=%s, version=%s, file=%s]', *info)

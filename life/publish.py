# coding: utf-8
import json

from common import logger
from common.request.file import upload
from constants.constants import *
from model.context import Context


def publish(context: Context):
    context.load()
    logger.debug('publish. [arg=%s, info=%s, packages=%s]',
                 context.args, context.pack.info, json.dumps(context.pack.packages, default=vars))
    ci = context.pack.info

    for module in context.pack.packages:
        if context.args.module and context.args.module != module.module:
            continue

        info = module.module, ci.space, ci.product, module.module, ci.version, module.file
        logger.info('prepare to upload package. [name=%s, space=%s, product=%s, '
                    'module=%s, version=%s, file=%s]', *info)
        dst = URL_META_PUB + '/' + ci.space if not context.args.meta else URL_EUBALAENA_PUB
        assert upload(dst, {
            'space': ci.space,
            'product': ci.product,
            'module': module.module,
            'version': ci.version
        }, {}, module.file), \
            'upload package failed. [name=%s, space=%s, product=%s, module=%s, version=%s, file=%s]' % info
        logger.info('upload packaged success. [name=%s, space=%s, product=%s, '
                    'module=%s, version=%s, file=%s]', *info)

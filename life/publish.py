# coding: utf-8
import os

from common.common import logger
from common.common.request.file import upload
from life.life import config, STAGE_PUBLISH, K_PRODUCT, K_INFO, K_VERSION, K_MODULES, K_SPACE
from life.package.sample import PATH_MERLIN


def publish(args):
    logger.info('arg: %s, config: %s', args, config(STAGE_PUBLISH))
    cfg = config()
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

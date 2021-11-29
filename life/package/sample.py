# coding: utf-8
from common.common.file import ensure_path
from constants.constants import PATH_MERLIN
from life.package.pack import PackConfig, TarPack
from model.context import Context


def pack(context: Context, module: str, cfg):
    ensure_path(PATH_MERLIN)
    pc = PackConfig(module, **cfg)
    TarPack(context, pc).do()

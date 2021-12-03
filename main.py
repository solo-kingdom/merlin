#!/bin/bash
# coding: utf-8

import logging
from argparse import ArgumentParser

from common import logger
from life import package, build, publish, clean
from life.life import config
from model.context import Context
from model.subcommand import Subcommand

logger.level(logging.DEBUG)

subcommands: [str, Subcommand] = {}


def parse():
    """ parse args
    1. get subcommand
    2. call subcommand.do()
    """
    parser = ArgumentParser()
    subcommand = parser.add_subparsers(dest="subcommand", description="sub parser")
    add_module(subcommand, package())
    add_module(subcommand, build())
    add_module(subcommand, publish())
    add_module(subcommand, clean())

    args = parser.parse_args()
    if not args.subcommand:
        logger.error('subcommand not specified, use -h to get help.')
        exit(1)
    elif args.subcommand not in subcommands:
        logger.error('unknown subcommand. [subcommand={}]', args.subcommand)
        exit(1)
    else:
        context = Context(args, config())
        subcommands[args.subcommand].do(context)
        context.finish()


def add_module(subcommand, mod: Subcommand):
    """ add subcommand & call subcommand.resolve() & keep"""
    for name in mod.names:
        if name in subcommands:
            logger.warning('repeated subcommand name. [name={}]', name)
            continue
        mod.resolve(subcommand.add_parser(name, help=mod.hlp))
        subcommands[name] = mod


if __name__ == '__main__':
    parse()

#!/bin/bash
from argparse import ArgumentParser

from common.common import logger
from life import package, build
from model.subcommand import Subcommand

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

    args = parser.parse_args()
    if not args.subcommand:
        logger.error('subcommand not specified')
        exit(1)
    elif args.subcommand not in subcommands:
        logger.error('unknown subcommand. [subcommand={}]', args.subcommand)
        exit(1)
    else:
        subcommands[args.subcommand].do(args)


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

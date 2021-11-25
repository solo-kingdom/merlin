#!/bin/bash
import logging
from argparse import ArgumentParser

from model.subcommand import Subcommand
from pack import parse as pack_parse

subcommands: [str, Subcommand] = {}


def parse():
    """ parse args
    1. get subcommand
    2. call subcommand.do()
    """
    parser = ArgumentParser()
    subcommand = parser.add_subparsers(dest="subcommand", description="sub parser")
    add_module(subcommand, pack_parse())

    args = parser.parse_args()
    if not args.subcommand:
        logging.error('subcommand not specified')
        exit(1)
    elif args.subcommand not in subcommands:
        logging.error('unknown subcommand. [subcommand={}]', args.subcommand)
        exit(1)
    else:
        subcommands[args.subcommand].do(args)


def add_module(subcommand, mod: Subcommand):
    for name in mod.names:
        if name in subcommands:
            logging.warning('repeated subcommand name. [name={}]', name)
            continue
        mod.resolve(subcommand.add_parser(name, help=mod.hlp))
        subcommands[name] = mod


if __name__ == '__main__':
    parse()

# coding: utf-8
__all__ = [
    'parse'
]

import argparse

from model.subcommand import Subcommand


def parse():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    def do(args):
        print(str(args))

    return Subcommand(['pack', 'package'], resolve=resolve, do=do, hlp='package subcommand')

# coding: utf-8
__all__ = [
    'package'
]

import argparse

from life.build import build as bld
from life.pack import pack
from model.subcommand import Subcommand


def build():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['build'], resolve=resolve, do=bld, hlp='build subcommand')


def package():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['pack', 'package'], resolve=resolve, do=pack, hlp='package subcommand')

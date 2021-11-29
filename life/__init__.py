# coding: utf-8
__all__ = [
    'package',
    'build',
    'publish'
]

import argparse

from life.build import build as bld
from life.pack import pack
from life.publish import publish as pub
from model.subcommand import Subcommand


def build():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['build'], resolve=resolve, do=bld, hlp='build subcommand')


def package():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['pack', 'package'], resolve=resolve, do=pack, hlp='package subcommand')


def publish():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['pub', 'publish'], resolve=resolve, do=pub, hlp='publish subcommand')

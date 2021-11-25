# coding: utf-8
__all__ = [
    'package',
    'build',
    'deploy'
]

import argparse

from life.build import build as bld
from life.deploy import deploy as dpl
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


def deploy():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['deploy'], resolve=resolve, do=dpl, hlp='deploy subcommand')

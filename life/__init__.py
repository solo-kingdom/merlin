# coding: utf-8
__all__ = [
    'package',
    'build',
    'publish',
    'clean'
]

import argparse

from life.build import build as bld
from life.clean import clean as cln
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
        parser.add_argument('--meta', action='store_true', help='publish to meta')
        parser.add_argument('-m', '--module', help='specify module')

    return Subcommand(['pub', 'publish'], resolve=resolve, do=pub, hlp='publish subcommand')


def clean():
    def resolve(parser: argparse.ArgumentParser):
        parser.add_argument('-i', '--info', help='show module information')

    return Subcommand(['clean'], resolve=resolve, do=cln, hlp='clean subcommand')

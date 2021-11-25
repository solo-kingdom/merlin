# coding: utf-8


class Subcommand:
    def __init__(self, names, resolve, do, hlp):
        self.names = names
        self.resolve = resolve
        self.do = do
        self.hlp = hlp

    def parse(self):
        self.resolve()

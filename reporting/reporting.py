"""Manages a reporting directory."""

import os

class Reporting:

    figure_rel_path = 'figures/'

    def __init__(self, path):
        self.path = path

    @property
    def path(self): return self.path

    @path.setter
    def path(self, path):
        if path[len(path)-1] != os.sep: path += os.sep
        self.path = path

    @property
    def figure_path(self): return self.path

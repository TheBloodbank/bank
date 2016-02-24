#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from vamp.package import PackageBase

class Package(PackageBase):

    def __init__(self):
        self.name = "NeoVIM"
        self.package_name = "neovim"
        self.requires = []

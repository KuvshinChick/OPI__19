#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import pathlib

if __name__ == "__main__":
    # Подсчет файлов
    print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))

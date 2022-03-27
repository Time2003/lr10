#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {0, 1, 2, 3, 4}
    b = {3, 2, 1}
    print(a.issubset(b))
    print(a.issuperset(b))
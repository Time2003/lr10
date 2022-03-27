#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.union(b)
    print(c)
    a.update(b)
    print(a)
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.intersection(b)
    print(c)
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.difference(b)
    print(c)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {'set', 'str', 'dict', 'list'}
    b = ','.join(a)
    print(b)
    print(type(b))
    a = {('a', 2), ('b', 4)}
    b = dict(a)
    print(b)
    print(type(b))
    a = {1, 2, 0, 1, 3, 2}
    b = list(a)
    print(b)
    print(type(b))
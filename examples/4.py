#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {0, 1, 2, 3}
    print(len(a))
    a.add(4)
    print(a)
    a = {0, 1, 2, 3}
    a.remove(3)
    print(a)
    a = {0, 1, 2, 3}
    a.clear()
    print(a)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"b", "e", "g", "h", "k", "s"}
    B = {"c", "g", "p", "q"}
    C = {"f", "g", "s", "x", "y", "z"}
    D = {"a", "c", "d", "g", "u", "v", "z"}
    X = (A.union(B)).intersection(C)
    print(f"x = {X}")
    an = u.difference(A)
    Y = (an.intersection(D)).union(C.difference(B))
    print(f"y = {Y}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    universum = set("аоуыэяёюие")
    k = 0
    s = input("Enter the string: ").lower()
    for ch in s:
        if ch in universum:
            k = k + 1
    print(f"There are {k} vowels in this string")
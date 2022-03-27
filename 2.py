#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(i for i in input("Enter the first string: ").lower())
    b = set(i for i in input("Enter the second string: ").lower())
    print(f"The intersection of these strings is: {a.intersection(b)}")
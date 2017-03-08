#!/usr/bin/env python3
# -*- coding: utf-8 -*-

max = int(input('Insert level: '))

def yanghui(max):
    L = [1]
    n = 1
    while n <= max:
        yield L
        L.append(1)
        K = tuple(L)
        for i in range(len(K)):
            L[i] = K[i-1] + K[i]
        L[0] = 1
        L[len(L) - 1] = 1
        n = n + 1

a = yanghui(max)
for k in range(max):
    print(next(a))
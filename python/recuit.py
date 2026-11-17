#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:47:07 2026

@author: yanis
"""


import random
import math


def f(x):
    return x ** 2

def recuit_simule():
    x1 = 50
    T = 1000
    i = 0
    xbest = x1
    n = 4
    TB = 0.01
    NTF = 5

    valeurs = []

    while T > TB:
        i = 0

        while i < NTF:
            x2 = x1 + random.uniform(-n, n)

            delta = f(x2) - f(x1)

            if delta < 0:
                x1 = x2

                if f(xbest) - f(x1) > 0:
                    xbest = x1

            else:
                if random.uniform(0,1) < math.exp(-delta / T):
                    x1 = x2

            valeurs.append(x1)
            i += 1

        T = 0.99 * T



    return xbest


xbest = recuit_simule()

print("Meilleure solution :", xbest)

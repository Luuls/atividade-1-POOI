# -*- coding: utf-8 -*-

a_WEIGHT = 3.5
b_WEIGHT = 7.5

a = float(input())
b = float(input())

average = (a * a_WEIGHT + b * b_WEIGHT) / (a_WEIGHT + b_WEIGHT)

print(f'MEDIA = {average:.5f}')

# -*- coding: utf-8 -*-

a_WEIGHT = 2
b_WEIGHT = 3
c_WEIGHT = 5

a = float(input())
b = float(input())
c = float(input())

average = (a * a_WEIGHT + b * b_WEIGHT + c * c_WEIGHT) / (a_WEIGHT + b_WEIGHT + c_WEIGHT)

print(f'MEDIA = {average:.1f}')

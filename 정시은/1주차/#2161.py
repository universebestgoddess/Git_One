# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:19:47 2022

@author: alaco
"""

card = int(input())
card_list = [i for i in range(1, card + 1)]
trash = []
while len(card_list) != 1:
    trash.append(card_list.pop(0))
    card_list.append(card_list.pop(0))
for i in trash:
    print(i)
print(card_list[0])


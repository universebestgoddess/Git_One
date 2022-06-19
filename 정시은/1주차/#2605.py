# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:11:47 2022

@author: alaco
"""

student= int(input())
arr=[]
#학생들이 뽑은 번호를 num에 입력받기
num= list(map(int,input().split()))
for i in range(student):
	arr.insert(i-num[i],i+1)
for k in arr:
	print(k)
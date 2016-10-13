#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s=[x**2 for x in range(1,101)]
print(list(s),end='\n\n')

s=[[x**2,x**3] for x in range(1,10)]
for i in s:
    print(i)

s=[(x,y) for x in range(1,10) for y in range(1,4)]
for i in s:
    print(i)

print()

s=[(x,y) for x in range(1,10) for y in range(1,4) if y != 2]
for i in s:
    print(i)

print()

m=[
[1,2],
[3,4],
[5,6],
[7,8],
 ]
s=[[row[i] for row in m] for i in range(len(m[0]))]
print(list(s))

#!/usr/bin/python
"""
Creado para Agora-security.com
2015
"""


f1=open("1","r")
f2=open("2","r")
f3=open("3","r")
final=open("final.dic","w")

F1=f1.readlines()
F2=f2.readlines()
F3=f3.readlines()
for l1 in F1:
	for l2 in F2:
		for l3 in F3:
			final.write(l1[:-1]+l2[:-1]+"."+l3)
			final.write(l1[:-1]+l2[:-1]+l3)
f1.close()
f2.close()
f3.close()
final.close()

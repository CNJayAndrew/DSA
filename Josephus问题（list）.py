#先来个简单的用列表写一下
import random
l=[]
for i in range(1,11) :
    l.append(str(i))

def Josephus(list,num) : #num的意思是第几个人去自杀。
    while len(list) !=1 :
        for i in range(num-1) :
            list.append(list.pop(0))
        print("第",list.pop(0),"号自杀了")
    return print(list)

Josephus(l,3)
import random 
l = []
for i in range(10) :
    l.append(random.randint(1,100))
print(l)
def insertsort(list) : 
    #插入排序是一个比较简单的排序，就是拿出来第一个元素，从他下一个往后比。循环也很好写。
    length = len(l)
    for i in range(length) :
        for j in range(i+1,length) :
            if list[i] > list[j] :
                list[i],list[j] = list[j],list[i]
    return print(list)

insertsort(l)
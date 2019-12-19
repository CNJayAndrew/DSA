import random 
l = []
for i in range(5) :
    l.append(random.randint(1,100))
print(l)
def selectsort(list) :
    length = len(list)
    for i in range (length-1) :
        min_inx = i 
        #假设最小的数的索引号为i，第一轮后i为2，已经把最小的放在第一个位置，第二轮就跳过了第一个位置（列表中最小的），可以寻找列表中第二小的。
        for j in range(i+1,length) : 
            #因为i是从第一个开始的，从i后面开始遍历，可以遍历后面所有元素
            if list[min_inx] > list[j] :
                min_inx = j #确定了最小那个数的index
        list[i],list[min_inx] = list[min_inx],list[i] # 在上层循环中，调换位置。
        
    return print(list)

selectsort(l)
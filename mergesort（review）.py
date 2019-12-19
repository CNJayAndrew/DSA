#这里采用了归并的思想，正常人的思路都是先分后和。所以先看下面的函数，后看上面的。
def merge(list1,list2) :
    templist = [] #这里创建的list是为了之后储存排序好的列表。
    h = j = 0 #我们要从每个列表的0号位，也就是第一个数开始比较。
    
    while h<len(list1) and j<len(list2) : #当这两个列表没有比较完的时候，循环不停止。
        if list1[h] < list2[j] : #举例，当list1和list2相比较的时候，如果list1的大，则在templist中加入list1中的数。
            templist.append(list1[h])
            h+=1
        else : #和上面意思差不多。
            templist.append(list2[j])
            j+=1
    
    if h == len(list1) :
        for i in list2[j:] :
            templist.append(i)
    else :
        for i in list1[h:] :
            templist.append(i)
    return templist

def mergesort(list):
    n = len(list)
    if n <= 1 :
        return list
    mid  = n//2
    left = mergesort(list[:mid]) #上边的都比较简单，这里采用了递归的思想，把一分为二的list继续往下分。
    right = mergesort(list[mid:])
    return merge(left,right)#这个函数负责合并。往上看

a=[3,5,1,8,9,2]
print(mergesort(a))
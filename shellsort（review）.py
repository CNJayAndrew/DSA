def shellsort(list) :
    length = len(list)
    gap = length//2
    while gap > 0 :
        for i in range(gap,length) :
            for j in range(i,0,-gap) :
                if list[j] < list[j - gap] :
                    list[j],list[j-gap] = list[j-gap],list[j]
                else :
                    break
        gap //= 2

l=[23,43,123,53,1,2,45]
shellsort(l)
print(l)
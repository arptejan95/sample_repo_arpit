import math
def bin_search(list, element):
    bottom = 0
    top = len(list)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if list[mid]==element:
            index = mid
        elif list[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

li=[2,5,7,9,11,17,222]
print(bin_search(list,11))
print(bin_search(list,12))

#Merge lists 1
list1=[1, 2, 3, 5, 6, 7, 8]
list2=[1, 5, 6, 7, 10, 13, 16, 20]
def merge(list1, list2):
    result=list1+list2
    result.sort()
    return result
print(merge(list1, list2))
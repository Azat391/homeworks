#Merge lists 2
def quick_merge():
    n=int(input())
    result=[]
    for i in range(n):
        list1=map(int, input().split())
        for j in list1:
            result.append(str(j))
    result.sort()
    result=' '.join(result)
    return result
print(quick_merge())
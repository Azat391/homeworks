#Делители 1
def get_factors(num):
    c=[]
    for i in range(1,num):
        if num%i==0:
            c.append(i)
    return c
num=int(input())
print(get_factors(num))
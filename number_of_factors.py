#Делители 2
def number_of_factors():
    num=int(input())
    c=[]
    for i in range(1,num):
        if num%i==0:
            c.append(i)
    return len(c)
print(number_of_factors())
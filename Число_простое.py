# Is the Number Prime?
def is_prime(num):
    c=1
    n=0
    for _ in range(num):
        c+=1
        if num%c==0:
            n+=1
    return True if n==1 else False
num=int(input())
print(is_prime(num))
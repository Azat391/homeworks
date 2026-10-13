# Next Prime
num=9
def get_next_prime(num):
    for i in range(100000):
        num+=1
        c=1
        n=0
        for _ in range(num):
            c+=1
            if num%c==0:
                n+=1
        final=num
        if n==1:
            break
    return final
print(get_next_prime(num))
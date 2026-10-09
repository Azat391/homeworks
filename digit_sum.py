#Сумма цифр
def print_digit_sum(num):
    num=str(num)
    sum=0
    for i in list(num):
        sum+=int(i)
    print(sum)
num=int(input())
print_digit_sum(num)
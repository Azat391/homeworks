# Сумма квадратов
def sq_sum(*args):
    result=0
    if args:
        for i in args:
            result.append(i**2)
        result=sum(result)
    else:
        result=0
    return result
args=map(int, input().split())
print(sq_sum(*args))
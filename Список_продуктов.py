# Список продуктов
def print_products(*args):
    result=[]
    n=0
    for i in args:
        if type(i)==str:
            result.append(i)
    if len(result)!=0:
        for i in result:
            n+=1
            print(f'{n}'+') '+f'{i}')
    else:
        print('Нет продуктов')
print_products('dsdsd',3232,'',None, True, 'eee')
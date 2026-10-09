#Найти всех 👀
def find_all(target, symbol):
    result=[]
    index=0
    for i in target:
        if i==symbol:
            result.append(index)
        index+=1
    return result
target=input()
symbol=input()
print(find_all(target, symbol))
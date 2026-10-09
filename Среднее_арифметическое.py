# Среднее арифметическое
def mean(*args):
    result=[]
    for i in args:
        if type(i)==int or type(i)==float:
            result.append(i)
    return sum(result)/len(result)

print(mean(5,'ewwe', 3))
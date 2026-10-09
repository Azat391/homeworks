#Количество аргументов
def count_args(*args):
    return len(args)
args=input().split()
print(count_args(*args))
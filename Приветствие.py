#    Приветствие
def greet(*args):
    result=[]
    for i in args:
        result.append(i)
    print('Привет,'+' and '.join(result))
args=[]
while True:
    c=input()
    if c=='':
        break
    args.append(c)
greet(*args)
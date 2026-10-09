# Именнованные аргументы
def info_kwargs(**kwargs):
    for i,j in kwargs.items():
        print(f'{i}: '+f'{j}')
kwargs={}
while True:
    key=input()
    if key=='':
        break
    values=input()
    kwargs[key]=values
info_kwargs(**kwargs)
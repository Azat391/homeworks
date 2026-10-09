def matrix(n=1, m=None, value=0):
    result=[]
    prom_result=[]
    if m==None:
        m=n
    for i in range(n):
        prom_result=[]
        for j in range(m):
            prom_result.append(value)
        result.append(prom_result)
        
    return result
print(matrix(n=5,m=2,value='eee'))
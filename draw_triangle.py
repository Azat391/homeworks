#Звёздный треугольник
def draw_triangle(fill, base):
    for i in range(1,((base+1)//2)+1):
        print(f'{fill}'*i)
    for i in range(((base+1)//2)-1,0,-1):
        print(f'{fill}'*i)
fill=input()
base=int(input())
draw_triangle(fill, base)
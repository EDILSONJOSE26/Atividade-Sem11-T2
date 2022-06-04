div = 0
a = 1
b = 1
s = 0
entrada = int(input().strip())
while s < entrada:
    b+=1
    div = a / b
    s +=div
    if b >= entrada:break
print(f'{1+s:.4f}')

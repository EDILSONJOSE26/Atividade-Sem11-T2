num = int(input().strip())
c = 0
for i in range(1, num + 1):
    if num % i == 0 :
        c += 1

if c == 2:
    print('True')
else:
    print('False')

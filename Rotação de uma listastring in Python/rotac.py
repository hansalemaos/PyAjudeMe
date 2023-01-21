from time import sleep
i = 'Oi, tudo bem? '
n=100

for _ in range(n):
    i = i[-1:] + i[:-1]
    print(i, end='\r')
    sleep(.1)

print('----------------')
print('----------------')


for _ in range(n):
    i = i[1:] + i[:1]
    print(i, end='\r')
    sleep(.1)
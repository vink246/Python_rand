n = 9
if n == 1:
    print (1)
startpow = 0
for i in range (1,n+1):
    i2 = i
    c = 0
    while i2 >= 10:
        i2 = i2/10
        c = c+1
        
    startpow = startpow+1+c
startpow = startpow-1

final = 1
for _ in range (1,startpow+1):
        final = final*10

c = 0
for i in range (2,n+1):
    i2 = i
    power = 1
    while i2 >= 10:
        i2 = i2/10
        c = c+1
    startpow = startpow-c
    for _ in range (1,startpow):
        power = power*10
    c = 1
    final = final+(i*power)

print(final)

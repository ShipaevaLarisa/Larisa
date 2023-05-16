print('x = ', end='')
x = float(input())
if x > 0:
    y = x - 2
elif x == 0:
    y = 0
else:
    y = abs(x)
print('y =',y)
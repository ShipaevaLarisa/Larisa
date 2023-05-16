a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))
m = a
if m < b:
    m = b
if m < c:
    m = c
print(m)
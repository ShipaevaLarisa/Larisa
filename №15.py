print('Введите количество строк и столбцов через пробел: ')
n, m = list(map(int, input().split()))
print('Ввведите элементы матрицы')
s = 0
for i in range(n):
    a = list(map(int,input().split()))
    s += sum(a)
print('Сумма элементов матрицы =', s)

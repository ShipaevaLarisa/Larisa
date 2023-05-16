count = int(input('Введите количество элементов в массиве: '))
numbers = []
for i in range(count):
    number = int(input())
    numbers.append(number)
print('Сумма элементов массива =', sum(numbers))
prod = 1
for elem in numbers:
    prod *= elem
print('Произведение элементов массива =', prod)

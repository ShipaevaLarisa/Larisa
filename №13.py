count = int(input('Введите количество элементов в массиве: '))
numbers = []
for i in range(count):
    number = int(input())
    numbers.append(number)
for i in range(len(numbers)):
    print(numbers[i] * -1, end=(' '))

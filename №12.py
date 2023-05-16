count = int(input('Введите количество элементов в массиве: '))
numbers = []
for i in range(count):
    number = int(input())
    numbers.append(number)
for i in range(len(numbers)):
    if numbers[i] > 0:
        print('Номер первого положительного элемента =', i+1)
        print('Его значение =', numbers[i])
        break


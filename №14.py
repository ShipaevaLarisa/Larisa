count = int(input('Введите количество элементов в массиве: '))
numbers = []
for i in range(count):
    number = int(input())
    numbers.append(number)
for i in range(len(numbers)):
    max_number = max(numbers)
    min_number = min(numbers)
index_max = numbers.index(max_number)
index_min = numbers.index(min_number)
numbers[index_max] = min_number
numbers[index_min] = max_number
print(numbers)

n = input("Введите число: ")
summa=sum(int(i)  for i in n if i in '2468')
print(f"Результат = {summa}")
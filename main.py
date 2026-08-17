# ДЗ Управление потоком

# Задание 1. Зеркальное отражение цифр
num = ""
while len(num) != 5:
    num = input("Введите пятизначное число:")
    if len(num) == 5:
        print(num[0],num[-2:-5:-1],num[4],sep = "")
        break
    elif len(num) < 5:
        print("Вы ввели менее пяти чисел")
    else:
        print("Вы ввели более пяти чисел")

# Задание 2. Подсчет выходных до отпуска

amount = int(input("Введите количество дней, оставшиеся до отпуска:"))
counter = 0
weekdays = 0
for i in range(0,amount):
    counter += 1
    if counter == 6:
        weekdays += 1
    elif counter == 7:
        weekdays += 1
        counter = 0
print(f"выходные {weekdays}")

# Задание 3. Плитка шоколада

length = int(input("Введите длину плитки: "))
width = int(input("Введите ширину плитки: "))
piece = int(input("Введите размер куска: "))

chok = length * width

if piece < chok and (piece % length == 0 or piece % width == 0):
    print(True)
else:
    print(False)

# Задание 4. Римские числа

rim_num = int(input("Введите целое положительное число: "))
count = 0
result = ''
for i in [1000,100,10,1]:
    count = rim_num // i
    if count >= 1:
        if i == 1000:
            result += 'M' * count
        else:
            if count == 9:
                if i == 100:
                    result += 'CM'
                if i == 10:
                    result += 'XC'
                if i == 1:
                    result += 'IX'
            if count > 5 and count < 9:
                if i == 100:
                    result += 'D' + ('C' * (count - 5))
                if i == 10:
                    result += 'L' + ('X' * (count - 5))
                if i == 1:
                    result += 'V' + ('I' * (count - 5))
            if count == 5:
                if i == 100:
                    result += 'D'
                if i == 10:
                    result += 'L'
                if i == 1:
                    result += 'V'
            if count == 4:
                if i == 100:
                    result += 'CD'
                if i == 10:
                    result += 'XL'
                if i == 1:
                    result += 'IV'
            if count > 0 and count < 4:
                if i == 100:
                    result += 'C' * count
                if i == 10:
                    result += 'X' * count
                if i == 1:
                    result += 'I' * count
        rim_num = rim_num%(i * count)
print(result)

# Задание 5. Проверка на вещественное число

num = input("Введите число: ")
result = False
counter = 0
point_count = 0
for i in num[::]:
    counter += 1
    if i == "." and counter == 1:
        result = False
        break
    elif i == "." and counter != 1 and counter != len(num):
        result = True
        point_count += 1
    elif i == "." and counter != 1 and counter == len(num):
        result = False

    if point_count > 1:
        result = False
        break

print(result)



biggest_palindrom = 0

for num1 in range(999, 0, -1):
    for num2 in range(999, 0, -1):
        if str(num1*num2) == str(num1*num2)[::-1] and num1*num2 > biggest_palindrom:
            biggest_palindrom = num1*num2

print(biggest_palindrom)
#task1
def calculate_expression(a, b):
    if a > b:
        return a * b + 1
    elif a == b:
        return 25
    elif b > a:
        return (a - 5) / b
    else:
        return "Невідома умова"


a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
result = calculate_expression(a, b)
print(f"Результат: {result}")


#task2
def fibonacci_sequence(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers


n = 8
fibonacci_numbers = fibonacci_sequence(n)
print("Перші 8 чисел ряду Фібоначчі:", fibonacci_numbers)
sum_fibonacci = sum(fibonacci_numbers)
print(f"Сума перших {n} чисел ряду Фібоначчі: {sum_fibonacci}")
# task3
N = int(input("Введіть число N (1 < N < 9): "))
if 1 < N < 9:
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
else:
    print("Число повинно бути більше за 1 і менше за 9!")

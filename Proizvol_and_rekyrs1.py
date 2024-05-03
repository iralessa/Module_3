def test_func(*args, **values):
    print("позиционные аргументы:")
    for arg in args:
        print(arg)
    print("именованные аргументы:")
    for key, value in values.items():
        print(f"{key}: {value}")

# вызов функции
test_func(1, "two", [3, 4, 5], surname="Leukhina", name="Irina", age=37)

print("**************************************************************************")

def factorial(n):
    # факториал 0 или 1 равен 1
    if n == 0 or n == 1:
        return 1
        print("факториал 0 или 1 равен 1")
    else:
        # вычисляем факториал от n как произведение n и (n-1)
        result = n * factorial(n - 1)
        if n-1 > 2:
            result1 = result//n
            print("вычисляем факториал как произведение ", n, " * ", result1, "=", result)
        else:
            print("вычисляем факториал как произведение ", n, " * ", n-1, "=", result)
        return result
# вызов функции для вычисления факториала
result2 = factorial(7)
print("Факториал равен:", result2)

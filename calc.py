print("'+' - сложение, '-' - вычитание, '*' - умножение, '/' - деление, '!' - факториал ")
operation = input('Операция: ')
x = float(input("Введите 'x': "))
if (operation != '!'):
    y = float(input("Введите число 'y': "))
    
result = None

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
        

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x ** y
elif operation == '/':
    result = x / y
elif operation == '!':
    result = factorial(x)
else:
    print('Вы ввели недопустимый символ(ы).Пожалуйста, введите простые числа')

if result is not None:
    print('Result:', result)
   

    def test_normal(self):
        res = x(float)
        self.assertEquals(x, float)
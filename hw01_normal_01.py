# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import random

random_integer = random.randint(1, 1000000)
print(random_integer)
max_integer = 0

while random_integer > 0:
    current_position = int(random_integer % 10)
    if current_position > max_integer:
        max_integer = current_position
    random_integer = int(random_integer / 10)

print('max_integer: ', max_integer)
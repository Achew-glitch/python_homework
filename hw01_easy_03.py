# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

old = int(input('Сколько Вам лет?\n'))
if old < 18:
    print('Извините, пользование данным ресурсом только с 18 лет')
else:
    print('Доступ разрешен')
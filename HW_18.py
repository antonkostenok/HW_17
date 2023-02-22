cost = 0
count_tiket = int(input('Введите колличество билетов '))
for i in range(count_tiket):
    i = i + 1
    age = int(input('Введите возраст посетителя по каждому билету '))
    if age < 18:
        print('Вход бесплатно ')
    elif 18 <= age < 25:
        cost += 990
        print('Вход 990 руб. ')
    else:
        cost += 1390
        print('Вход 1390 руб ')
print('Сумма покупки', + cost)
if count_tiket > 3:
    all_cost = cost - ((cost / 100) * 10)
print('Сумма покупки с учетом скидки ', + all_cost)
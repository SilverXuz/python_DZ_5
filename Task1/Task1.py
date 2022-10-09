"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""

import random

balance = 82
step = 8
print('1 - против бота')
print('2 - против игрока')
print('3 - против умного бота')
menu = int(input('Против кого хотите играть? Введите число: '))
while menu < 1 or menu > 3:
    menu = int(input('Введите число 1, 2 или 3: '))
if menu == 1:
    print('Вы играете против бота!')
    print()
    p1 = random.randint(2, 100)
    print(f'Жребий первого игрока: {p1}')

    p2 = random.randint(2, 100)
    print(f'Жребий бота {p2}')

    if p1 > p2:
        print('Начинает первый игрок!')
        p1 = 1
        p2 = 0
    elif p1 == p2:
        p1 = random.randint(2, 100)
        print(f'Жребий первого игрока: {p1}')

        p2 = random.randint(2, 100)
        print(f'Жребий умного бота {p2}')
    else:
        print('Начинает умный бот!')
        p2 = 1
        p1 = 0

    while balance > 0:       
        if p1 == 1:
            rate = int(input('Первый игрок, сколько конфет хотите взять? - '))
            while rate < 1 or rate > 8:
                rate = int(input('Первый игрок, можно взять от 1 до 8 конфет. Сколько конфет хотите взять? - '))
            p1 = 0
            p2 = 1
            balance = balance - rate
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p1 = 'первый игрок'
                print(f'Игра окончена, победил {p1}!')
        else:
            rate = random.randint(1, 8)
            print(f'Бот взял {rate} конфет(ы)')
            p2 = 0
            p1 = 1
            balance = balance - rate
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p2 = 'бот'
                print(f'Игра окончена, победил {p2}!')

elif menu == 2:
    print('Вы играете против игрока!')
    print()
    p1 = random.randint(2, 100)
    print(f'Жребий первого игрока: {p1}')

    p2 = random.randint(2, 100)
    print(f'Жребий второго игрока {p2}')

    if p1 > p2:
        print('Начинает первый игрок!')
        p1 = 1
        p2 = 0
    elif p1 == p2:
        p1 = random.randint(2, 100)
        print(f'Жребий первого игрока: {p1}')

        p2 = random.randint(2, 100)
        print(f'Жребий умного бота {p2}')
    else:
        print('Начинает умный бот!')
        p2 = 1
        p1 = 0

    while balance > 0:       
        if p1 == 1:
            rate = int(input('Первый игрок, сколько конфет хотите взять? - '))
            while rate < 1 or rate > 8:
                rate = int(input('Первый игрок, можно взять от 1 до 8 конфет. Сколько конфет хотите взять? - '))
            p1 = 0
            p2 = 1
            balance = balance - rate
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p1 = 'первый игрок'
                print(f'Игра окончена, победил {p1}!')
        else:
            rate = int(input('Второй игрок, сколько конфет хотите взять? - '))
            while rate < 1 or rate > 8:
                rate = int(input('Второй игрок, можно взять от 1 до 8 конфет. Сколько конфет хотите взять? - '))
            p2 = 0
            p1 = 1
            balance = balance - rate
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p2 = 'второй игрок'
                print(f'Игра окончена, победил {p2}!')

elif menu == 3:
    print('Вы играете против умного бота!')
    print()
    p1 = random.randint(2, 100)
    print(f'Жребий первого игрока: {p1}')

    p2 = random.randint(2, 100)
    print(f'Жребий умного бота {p2}')

    if p1 > p2:
        print('Начинает первый игрок!')
        p1 = 1
        p2 = 0
    elif p1 == p2:
        p1 = random.randint(2, 100)
        print(f'Жребий первого игрока: {p1}')

        p2 = random.randint(2, 100)
        print(f'Жребий умного бота {p2}')
    else:
        print('Начинает умный бот!')
        p2 = 1
        p1 = 0

    rate1 = 1
    while balance > 0:      
        if p1 == 1:
            rate1 = int(input('Первый игрок, сколько конфет хотите взять? - '))
            while rate1 < 1 or rate1 > 8:
                rate1 = int(input('Первый игрок, можно взять от 1 до 8 конфет. Сколько конфет хотите взять? - '))
            p1 = 0
            p2 = 1
            balance = balance - rate1
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p1 = 'первый игрок'
                print(f'Игра окончена, победил {p1}!')
        
        else:
            if balance == 82:
                rate = balance % (step + 1)
            elif balance <= 8:
                rate = balance
            else:
                rate = 9 - rate1

            print(f'Умный бот взял {rate} конфет(ы)')
            p2 = 0
            p1 = 1
            balance = balance - rate
            print(f'Осталось конфет: {balance}')
            if balance <= 0:
                p2 = 'умный бот'
                print(f'Игра окончена, победил {p2}!')

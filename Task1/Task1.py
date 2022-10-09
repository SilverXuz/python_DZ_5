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

p1 = random.randint(2, 100)
print(f'Жребий первого игрока: {p1}')

p2 = random.randint(2, 100)
print(f'Жребий второго игрока {p2}')

if p1 > p2:
    print('Начинает первый игрок!')
    p1 = 1
    p2 = 0
else:
    print('Начинает второй игрок!')
    p2 = 1
    p1 = 0

balance = 100
while balance > 0:       
    if p1 == 1:
        rate = int(input('Первый игрок, сколько конфет хотите взять? - '))
        while rate < 1 or rate > 28:
            rate = int(input('Первый игрок, можно взять от 1 до 28 конфет. Сколько конфет хотите взять? - '))
        p1 = 0
        p2 = 1
        balance = balance - rate
        print(f'Осталось конфет: {balance}')
        if balance <= 0:
            p1 = 'первый игрок'
            print(f'Игра окончена, победил {p1}!')
    else:
        rate = int(input('Второй игрок, сколько конфет хотите взять? - '))
        while rate < 1 or rate > 28:
            rate = int(input('Второй игрок, можно взять от 1 до 28 конфет. Сколько конфет хотите взять? - '))
        p2 = 0
        p1 = 1
        balance = balance - rate
        print(f'Осталось конфет: {balance}')
        if balance <= 0:
            p2 = 'второй игрок'
            print(f'Игра окончена, победил {p2}!')

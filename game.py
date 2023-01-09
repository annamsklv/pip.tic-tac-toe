# 3- Создайте программу для игры в ""Крестики-нолики"".
#  Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
from typing import List
from functions import give_int
import emoji


def draw_board(area: List) -> List:
    '''
    Функция, выводящая на консоль игровое поле из 9 пронумерованных клеток
    '''    
    print('│', area[1], '│', area[2], '│', area[3], '│')
    print('│', area[4], '│', area[5], '│', area[6], '│')
    print('│', area[7], '│', area[8], '│', area[9], '│')


def game(players: List, area: List) -> None:
    '''
    Логика игры
    arg players: список игроков
    arg area: список номеров клеток игрового поля
    '''   
    pl = players[0]
    for i in range(len(area) - 1):
        new_turn = 10
        while new_turn > 9 or area[new_turn] in (':cross_mark:', ':hollow_red_circle:'):
            new_turn = give_int(
                f'{pl[1]}, куда поставить отметку? Введите число от 1 до 9:', 1)
            if new_turn > 9 or emoji.is_emoji(area[new_turn]):
                print('Эта клетка уже занята\n')
        if pl == players[0]:
            area[new_turn] = emoji.emojize(':cross_mark:')
            draw_board(area)
            if i >= 4:
                check_win(area, players[0])
            pl = players[1]
        else:
            area[new_turn] = emoji.emojize(':hollow_red_circle:')
            draw_board(area)
            if i >= 4:
                check_win(area, players[1])
            pl = players[0]


def check_win(area: List, players: List) -> None:
    '''
    Функция, проверяющая выигрышные комбинации
    arg players: список игроков
    arg area: список номеров клеток игрового поля
    '''   
    if area[1] == area[2] == area[3]\
            or area[4] == area[5] == area[6]\
            or area[7] == area[8] == area[9]\
            or area[1] == area[4] == area[7]\
            or area[2] == area[5] == area[8]\
            or area[3] == area[6] == area[9]\
            or area[1] == area[5] == area[9]\
            or area[3] == area[5] == area[7]:
        return exit(print(f'{players[1]} победил!'))
    else:
        return


area = list(range(10))
pl1 = input('Введите имя первого игрока:\n')
pl2 = input('Введите имя второго игрока:\n')
players = [[1, pl1], [2, pl2]]
draw_board(area)
game(players, area)



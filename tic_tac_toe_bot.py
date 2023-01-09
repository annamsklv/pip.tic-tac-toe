from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
from config import TOKEN
# from game import area, draw_board
from strings import area

def start_game(update: Update, context: CallbackContext):
    after_command = context.args
    update.message.reply_text(area)
    print(after_command)

# def check_win(area: List, players: List) -> None:
#     '''
#     Функция, проверяющая выигрышные комбинации
#     arg players: список игроков
#     arg area: список номеров клеток игрового поля
#     '''   
#     if area[1] == area[2] == area[3]\
#             or area[4] == area[5] == area[6]\
#             or area[7] == area[8] == area[9]\
#             or area[1] == area[4] == area[7]\
#             or area[2] == area[5] == area[8]\
#             or area[3] == area[6] == area[9]\
#             or area[1] == area[5] == area[9]\
#             or area[3] == area[5] == area[7]:
#         return exit(print(f'{players[1]} победил!'))
#     else:
#         return



updater = Updater(TOKEN)
dispatcher = updater.dispatcher


game_handler = CommandHandler('start_game', start_game)

dispatcher.add_handler(game_handler)

print('Сервер запущен')
updater.start_polling()
updater.idle()
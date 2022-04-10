import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


#from commander.commander import Commander
from bot_vk import VkBot


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


if __name__ == '__main__':

    # API-ключ созданный ранее
    token = "Your API token here..."

    # Авторизуемся как сообщество
    vk = vk_api.VkApi(token=token)

    # Работа с сообщениями
    longpoll = VkLongPoll(vk)
    start_conditions = ""
    #commander = Commander()
    print("Server started")
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                print(f'Сообщение от  {event.user_id}', end='')
                bot = VkBot(event.user_id)
                write_msg(event.user_id, bot.new_message(event.text))
                print('Text: ', event.text)
                print("-------------------")
                if event.text.count(',') == 3:
                    start_conditions += event.text
    print(start_conditions)

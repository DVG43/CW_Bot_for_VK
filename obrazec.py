from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = input('Token: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7)})


for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
         # Если оно имеет метку для меня
        if event.to_me:
            request = event.text
            # Логика ответа
            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}, хотел бы подобрать партнера для общения ? да/нет")
            elif request == "да":
                write_msg(event.user_id, "Неоходимо внести возраст, пол, город, семейное положение ")
            elif request == "нет":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
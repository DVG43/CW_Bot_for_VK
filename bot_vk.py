import bs4 as bs4
import requests
from work_with_Api import search_piople_foto

class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОДБОР", "ПОКА"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):

        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!, если вы желаете подобрать партнера, наберите 'подбор', если " \
                   f"не желаете наберите 'пока'"
        # Подбор
        elif message.upper() == self._COMMANDS[1]:
            return f"Вам необходимо ввести возраст (полных лет), пол (м или Ж), город, семейное положение" \
                   f" (женат/замужем или не женат/не замужем или в активном поиске), ввод одной строкой через запятую "
        # Пока
        elif message.upper() == self._COMMANDS[2]:
            return f"Пока-пока, {self._USERNAME}!"
        elif message.upper().count(',') == 3:
            resalt_of_search = search_piople_foto(message.upper())
            return f"Результат поисков следующие люди и их фото :  {resalt_of_search}"

        else:
            return "Не понимаю о чем вы..."


    @staticmethod
    def _clean_all_tag_from_str(string_line):

        # Очистка строки stringLine от тэгов и их содержимых
        # :param string_line: Очищаемая строка
        # :return: очищенная строка

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result



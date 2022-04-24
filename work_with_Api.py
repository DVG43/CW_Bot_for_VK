import vk_api
import time
import requests


# по полученным данным определяем кандидатов
def serch_users(year_birth, sex, city, status):
    token_owner = 'b46a44cdd583b2cc46fa9e43c498c028975b8817c7a33aa5dbaa6a6fb751db00ccaf41586525a13db7891'
    vk_session = vk_api.VkApi(token=token_owner, api_version='5.131')
    get_users = vk_api.VkTools(vk_session)

    response = get_users.get_all('users.search',10, {
                                       'birth_year': year_birth,
                                       'sex': sex,
                                       'hometown': city,
                                       'status': status,
                                       'has_photo': 1
                                        }
                                    )
    return response



#получаем все доступные фото кандидатов.photos.getProfile photos.getAll
def serch_photo_for_person (person_id):
    token_owner = 'b46a44cdd583b2cc46fa9e43c498c028975b8817c7a33aa5dbaa6a6fb751db00ccaf41586525a13db7891'
    # vk_session = vk_api.VkApi(token=token_owner, api_version='5.131')
    # get_photo = vk_api.VkTools(vk_session)
    # #try:
    # resalt_photo = get_photo.get_all('photos.getProfile', 10,
    #                                  {'owner_id': person_id,
    #                                   'album_id': 'profile',
    #                                   'extended': 1
    #                                   }
    #                                  )
    # # except:
    # #     return "закрытый профиль"
    # return resalt_photo['items']

    URL = 'https://api.vk.com/method/photos.getAll'  # Получение фото
    params = {
        'owner_id': person_id,
        'album_id': 'profile',
        'extended': 1,
        'photo_sizes': 0,
        'access_token': token_owner,
        'v': '5.131'
    }
    fotos = requests.get(URL, params=params)
    resalt_foto = fotos.json()
    print(resalt_foto)
    return resalt_foto  #['items']

#resalt_photo = get_photo.get_all('photos.get', 10,

# выбираем нужные нам фото
def foto_dict_person (fotolist):
    personal_foto_list = []
    for one_foto in fotolist:
        foto_id = one_foto['id']
        count_liks = one_foto['likes']['count']
        count_reposts = one_foto['reposts']['count']
        url_str = one_foto['sizes'][-1]['url']
        foto_dikt = {'id': foto_id, 'url': url_str, 'liks': count_liks}
        personal_foto_list.append(foto_dikt)

    list_liks = []
    for foto in personal_foto_list:
        list_liks.append(foto['liks'])
    sort_list_liks = sorted(list_liks)
    sort_list_liks[:-3] = []
    print(sort_list_liks)

    short_foto_str = " "
    for foto in personal_foto_list:
        if foto['liks'] in sort_list_liks:
             short_foto_str += f"{foto['url']}"


    return short_foto_str


def search_piople_foto(string_date):
    start_list = string_date.split(',')
    year_of_birth = 2022 - int(start_list[0])
    if start_list[1] == 'ж' or 'w' or 'female' or 'f':
        index_sex = 1
    elif start_list[1] == 'м' or 'm' or 'male' or 'man':
        index_sex = 2
    else:
        return "неверный ввод пола"
    city = start_list[2]
    if start_list[3] == 'не женат' or 'не замужем':
        index_status = 1
    elif start_list[3] == 'женат' or 'замужем':
        index_status = 4
    elif start_list[3] == 'в активном поиске':
        index_status = 6
    else:
        return "неверный ввод статуса"
    list_piople = serch_users(year_of_birth, index_sex, city, index_status)['items']
    print(list_piople)

    result_str = ''
    for person in list_piople:
        id_for_person = str(person['id'])
        list_of_foto = serch_photo_for_person(id_for_person)
        time.sleep(5)
        if list_of_foto == "закрытый профиль":
            result_str += "закрытый профиль"
            continue
        else:
            fotos = foto_dict_person(list_of_foto)
            result_str += f" Имя {person['first_name']}"
            result_str += f" Фамилия {person['last_name']}"
            result_str += f" и фотографии {fotos} /// "

    return result_str
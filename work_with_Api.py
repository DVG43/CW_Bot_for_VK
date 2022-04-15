import vk_api
import vk
import json

def serch_users(year_birth, sex, city, status):

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

def serch_photo_for_person (person_id):
    get_photo = vk_api.VkTools(vk_session)
    resalt_photo = get_photo.get_all('photos.getAll', 3,
                                     {'owner_id': person_id,
                                      'extended': 1
                                      }
                                     )
    return resalt_photo


token_owner = '31f694b775b4be9a77eff1847b90175f8816a09ece569f2c41185c3d2da99a6cd826562dc4b3a5e46d19a'
vk_session = vk_api.VkApi(token=token_owner, api_version='5.131')
list_piople = serch_users(1985, 1, 'Санкт_Петербург', 1)['items']
print(list_piople)

for person in list_piople:
    aaa = str(person ['id'])
    print(serch_photo_for_person(aaa))

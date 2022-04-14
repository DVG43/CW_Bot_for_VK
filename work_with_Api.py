import vk_api
import vk
import json

def serch_users(year_birth, sex, city, status):
    token_owner = '*************************'

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

list_piople = serch_users(1985, 1, 'Санкт_Петербург', 1)['items']
print(list_piople)

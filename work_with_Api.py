import vk
import json

def serch_users(year_birth, sex, city, status):
    response = vk_api.users.siarch(sort=0,
                                   count=20,
                                   hometown=city,
                                   sex=sex,
                                   birth_year=year_birth,
                                   status=status,
                                   has_photo=1
                                   )
    return response

token_owner = '31f694b775b4be9a77eff1847b90175f8816a09ece569f2c41185c3d2da99a6cd826562dc4b3a5e46d19a'

session = vk.Session(access_token = token_owner)
vk_api = vk.API(session,v = 5.131)
response = vk_api.users.get(user_id = 1)
first_name = response[0]['first_name']
print(first_name)

print(serch_users(1981, 1, 'Санкт_петербург', 4))
# aaa = "30,ж,Санкт-Петербург,холост"
# bbb = aaa.split(',')
# print(bbb)
#
# proba_dist = {'album_id': -6, 'date': 1314409736, 'id': 266151641, 'owner_id': 81827423, 'post_id': 40, 'sizes':
# [{'height': 0, 'url': 'https://sun9-50.userapi.com/c5779/u81827423/-6/s_87c51d7d.jpg', 'type': 's', 'width': 0},
# {'height': 0, 'url': 'https://sun9-68.userapi.com/c5779/u81827423/-6/m_94dd1776.jpg', 'type': 'm', 'width': 0},
# {'height': 0, 'url': 'https://sun9-81.userapi.com/c5779/u81827423/-6/x_58cf07ec.jpg', 'type': 'x', 'width': 0},
# {'height': 0, 'url': 'https://sun9-4.userapi.com/c5779/u81827423/-6/y_03ad4cd5.jpg', 'type': 'y', 'width': 0},
# {'height': 0, 'url': 'https://sun9-84.userapi.com/c5779/u81827423/-6/z_214bb4b8.jpg', 'type': 'z', 'width': 0},
# {'height': 0, 'url': 'https://sun9-75.userapi.com/c5779/u81827423/-6/w_03151454.jpg', 'type': 'w', 'width': 0}],
# 'text': '', 'has_tags': False, 'likes': {'count': 24, 'user_likes': 0}, 'reposts': {'count': 1}}
#
# count_liks = proba_dist['likes']['count']
# count_reposts = proba_dist['reposts']['count']
# url_str = proba_dist['sizes'][-1]['url']
#
# print(count_liks)
# print(count_reposts)
# print(url_str)

list_liks = [23,34,12,3,45,66,8]
sort_list_liks = sorted(list_liks)
print(sort_list_liks)
sort_list_liks[:-3] = []
print(sort_list_liks)

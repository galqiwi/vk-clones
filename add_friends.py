from time import sleep
from bots import vk_apis, zero_id, accounts, captcha_handler, default_vk

friends_str = ''
with open('friends', 'r') as file:
	friends_str = file.read()

friends = [{'id': x.split(' #')[0], 'name': x.split(' #')[1]} for x in friends_str.split('\n')]

ids_ = ([x['id'] for x in (default_vk.users.get(user_ids=[x['id'] for x in friends]))])

for friend, id_ in zip(friends, ids_):
	print(friend['name'])
	print(friend)
	for vk in vk_apis:
		flag = True
		while flag:
			try:
				vk.friends.add(user_id=int(id_))
				flag = False
			except:
				print('error')
				sleep(10)
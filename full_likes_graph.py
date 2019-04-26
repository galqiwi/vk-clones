from time import sleep
from bots import vk_apis, zero_id, accounts, captcha_handler

counter = 0
for vk, account in zip(vk_apis, accounts):
	for friend in accounts:
		if friend['id'] != account['id']:
			continue
		print(counter, friend['id'], account['id'])
		for post in vk.wall.get(owner_id=friend['id'])['items']:
			flag = True
			while flag:
				try:
					vk.likes.add(type='post', owner_id=post['owner_id'], item_id=post['id'])
					flag = False
				except:
					print('failed on', counter)
					sleep(10)
					pass
		counter += 1

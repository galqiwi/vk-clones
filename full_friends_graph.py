from time import sleep
from bots import vk_apis, zero_id, accounts, captcha_handler

counter = 0
for vk, account in zip(vk_apis, accounts):
	for friend in accounts:
		if friend['id'] == account['id']:
			continue
		vk.friends.add(user_id=friend['id'], captcha_handler=captcha_handler)
		print(counter, friend['id'], account['id'])
		counter += 1
		sleep(1)

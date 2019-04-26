import json
import vk
import vk_api
from captcha import captcha_handler

with open('accounts.json', 'r') as file:
	data = json.loads(file.read())
	accounts = data['accounts']
	zero_id = int(data['zero_id'])

vk_apis = []
def init_apis():
	current_id = 0
	for account in accounts:
		vk_session = vk_api.VkApi(account['phone'], account['password'], captcha_handler=captcha_handler)
		vk_session.auth()
		vk_apis.append(vk_session.get_api())
		print('account', current_id, 'successfully inited')
		current_id += 1
init_apis()

default_vk = vk_apis[0]
from time import sleep
from bots import vk_apis, zero_id, accounts, captcha_handler, default_vk
import requests
import json
import functools

wall = default_vk.wall.get(owner_id=zero_id)

def less_than_id(x, y):
	return x['id'] < y['id']

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

def wipeWall(vk):
	posts = [r['id'] for r in vk.wall.get(count=100)['items']]
	print(posts)
	for post in posts:
		vk.wall.delete(post_id=post)

for vk in vk_apis:
	wipeWall(vk)

for i in sorted(wall['items'], key=functools.cmp_to_key(make_comparator(less_than_id))):
	message = i['text']
	attachments = []
	attachments_str = ''
	if 'attachments' in i.keys():
		for attachment in i['attachments']:
			if 'photo' in attachment.keys():
				attachments.append({'photo': attachment['photo']})
			else:
				attachments.append({attachment['type']: attachment})
	else:
		pass
	if 'geo' in i.keys():
		attachments.append({'geo': i['geo']})
	geo = False
	lat_ = 0
	long_ = 0
	for attachment in attachments:
		type_ = list(attachment.keys())[0]
		val_ = attachment[type_]
		if type_ == 'photo':
			attachments_str += 'photo'
			attachments_str += str(val_['owner_id'])
			attachments_str += '_'
			attachments_str += str(val_['id'])
			attachments_str += ','
		
		if type_ == 'video':
			attachments_str += 'video'
			attachments_str += str(val_['video']['owner_id'])
			attachments_str += '_'
			attachments_str += str(val_['video']['id'])
			attachments_str += ','

		if type_ == 'poll':
			attachments_str += 'poll'
			attachments_str += str(val_['poll']['owner_id'])
			attachments_str += '_'
			attachments_str += str(val_['poll']['id'])
			attachments_str += ','

		if type_ == 'geo':
			geo = True
			lat_, long_ = [float(x) for x in val_['coordinates'].split(' ')]

	attachments_str = attachments_str[:-1]

	if 'copy_history' in i.keys():
		object_id = 'wall' + str(i['copy_history'][0]['owner_id']) + '_' + str(i['copy_history'][0]['id'])
		for vk in vk_apis:
			vk.wall.repost(object=object_id, message=message, attachments=attachments_str)
	else:
		if geo:
			for vk in vk_apis:
				vk.wall.post(message=message, attachments=attachments_str, lat=lat_, long=long_)
		else:
			if attachments_str == '':
				for vk in vk_apis:
					vk.wall.post(message=message)
			else:
				for vk in vk_apis:
					vk.wall.post(message=message, attachments=attachments_str)
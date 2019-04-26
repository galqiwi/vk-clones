from time import sleep
from bots import vk_apis, zero_id, accounts, default_vk

videos = default_vk.video.get(owner_id=zero_id, count=100)

counter = 0
for vk in vk_apis:
	for video in videos['items']:
		vk.video.add(video_id=video['id'], owner_id=video['owner_id'])
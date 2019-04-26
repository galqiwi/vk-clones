from time import sleep
from bots import vk_apis, zero_id, accounts, captcha_handler
import requests
import json

photo_raw = requests.get('https://pp.userapi.com/c847216/v847216058/713d8/aw2dx2YMOU4.jpg').text

def change_photo(vk):
	upload_url = vk.photos.getOwnerPhotoUploadServer()['upload_url']
	answer = json.loads(requests.post(upload_url, files={'photo': open('avatar.jpg', 'rb')}).text)
	vk.photos.saveOwnerPhoto(photo=answer['photo'], server=answer['server'], hash=answer['hash'])

counter = 0
for vk in vk_apis:
	change_photo(vk)
	print(counter, 'done')
	counter += 1
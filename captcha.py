import requests
import base64
from time import sleep

RUCAPTCHA_KEY = "RUCAPTCHA_KEY"
def uncapcha(url):
	imager = requests.get(url)
	r = requests.post('http://rucaptcha.com/in.php', data = {'method': 'base64', 'key': RUCAPTCHA_KEY, 'body': base64.b64encode(imager.content)})
	if (r.text[:3] != 'OK|'):
		print('captcha failed')
		return -1
	capid = r.text[3:]
	sleep(5)
	capanswer = requests.post('http://rucaptcha.com/res.php', data = {'key': RUCAPTCHA_KEY, 'id':capid, 'action':'get'}).text
	if (capanswer[:3] != 'OK|'):
		print('captcha failed')
		return -1
	return capanswer[3:]


def captcha_handler(captcha):
	key = uncapcha(captcha.get_url())
	return captcha.try_again(key)
from time import sleep
from bots import vk_apis, zero_id, accounts, default_vk

groups = default_vk.groups.get(user_id=zero_id, count=100)

print(groups)

counter = 0
for vk in vk_apis:
	for group in groups['items']:
		try:
			print('add to', group)
			vk.groups.join(group_id=group)
		except:
			pass
	print(counter)
	counter += 1
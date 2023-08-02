#from mqtt
import lib_mqtt as ipc
import random

id = random.randrange(1, 1000)
print(id)
user = ipc.connect(f'3-{id}', '1')
user.on_message = ipc.on_message
ipc.subscribe('1', 0)
ipc.publish('1', 'Howdy pardner!', 0)
ipc.disconnect(f'{id}')

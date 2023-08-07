#from mqtt
import lib_mqtt as ipc
import random

id = '3-'+str(random.randrange(1, 1000))
user = ipc.connect(id, '1')
user.on_message = ipc.on_message
user.on_subscribe = ipc.on_subscribe
user.on_disconnect = ipc.on_disconnect
user.on_publish = ipc.on_publish
ipc.subscribe('1', 0)
ipc.publish('1', 'Howdy pardner!', 0)
#ipc.disconnect(id)

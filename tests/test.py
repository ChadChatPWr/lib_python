from mqtt import lib_mqtt as ipc
import random

id = random.randrange(1, 1000)
ipc.connect(f"3-{id}", "3")
ipc.subscribe('1', 0)
ipc.publish('1', "chujowa sprawa bracie", 0)
ipc.disconnect(f'{id}')
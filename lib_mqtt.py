# component_id is the identification for subsequent component that would interfere with the broker.
# the numbers shall be randomly generated as follows: 1-10000

import paho.mqtt.client as mqtt

broker_address = '127.0.0.1'
broker_port = ''

client = mqtt.Client()


def connect(component_id: int):
    global client
    client = mqtt.Client(component_id)
    client.connect(broker_address, broker_port, 60)


def renew(component_id: int):
    client.reinitialise(client_id=component_id, clean_session=True, userdata=None)


def disconnect(component_id: int):
    client.disconnect()


def publish(topic: int, data: str, qos: int):
    client.publish(topic, data, qos, retain=False)


def subscribe(topic: int, qos: int):
    client.subscribe(topic, qos)


def unsubscribe(topic: int):
    client.unsubscribe(topic)


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+str(rc))


def on_message(client, userdata, msg):
    print("Received message from: " + msg.topic + " with QoS " + str(msg.qos))


def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Connection closed by the client.")
    else:
        print("Connection closed unexpectedly")


def on_publish(client, userdata, mid):
    print("Succesfully received the message from "+client)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Succesfully subscribed to the topic")


def on_unsubscribe(client, userdata, mid):
    print("Succesfully unsubscribed from the topic")


client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
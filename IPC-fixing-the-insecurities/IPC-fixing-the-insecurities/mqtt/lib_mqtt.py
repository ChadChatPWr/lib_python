# component_id is the identification for subsequent component that would interfere with the broker.
# the numbers shall be randomly generated as follows: 1-10000

import paho.mqtt.client as mqtt
import random
broker_address = '127.0.0.1'
broker_port = 10234

client = mqtt.Client()


def is_topic(nr: str):
    nr = int(nr)
    if 0 < nr < 6:
        return True
    else:
        return False


def is_qos(nr: int):
    if -1 < nr < 3:
        return True
    else:
        return False


def connect(component_id: str, topic: str):
    global client
    client = mqtt.Client(client_id=component_id, clean_session=False, userdata=None, protocol=4,)
    client.will_set(topic)
    client.connect(broker_address, broker_port, 60)


def renew(component_id: str):
    client.reinitialise(client_id=component_id, clean_session=True, userdata=None)


def disconnect(component_id: str):
    client.disconnect()


def publish(topic: str, data: str, qos: str):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    if not (is_qos(qos)):
        print("Invalid Qos number!")
        return 1
    res, mid = client.publish(topic, data, qos, retain=False)
    if res == mqtt.MQTT_ERR_SUCCESS:
        print("Publish sent successfully")
    else:
        print("Publish failed with code: " + res)


def subscribe(topic: str, qos: str):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    if not (is_qos(qos)):
        print("Invalid Qos number!")
        return 1
    client.subscribe(topic, qos)


def unsubscribe(topic: str):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
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
    print("Successfully received the message from "+client)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Successfully subscribed to the topic")


def on_unsubscribe(client, userdata, mid):
    print("Successfully unsubscribed from the topic")


client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe

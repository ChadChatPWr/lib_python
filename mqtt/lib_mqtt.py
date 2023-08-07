# component_id is the identification for subsequent component that would interfere with the broker.
# the numbers shall be randomly generated as follows: 1-10000

import paho.mqtt.client as mqtt

broker_address = '127.0.0.1'
broker_port = 1883

client = None
client_component_ids = {}


def is_topic(nr: str):
    if 0 < int(nr) < 6:
        return True
    else:
        return False


def is_qos(nr: int):
    if -1 < nr < 3:
        return True
    else:
        return False


def is_compid(nr: str):
    if 0 < int(nr[0]) < 4:
        return True
    else:
        return False


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
    component_id = client_component_ids.get(client, "Unknown")
    print(f"Successfully received the message with MID: {mid} from client: {component_id}")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Successfully subscribed to topic: ", userdata["subscribed_topic"])


def on_unsubscribe(client, userdata, mid):
    print("Successfully unsubscribed from the topic")


def connect(component_id: str, topic: str):
    if not (is_compid(component_id[0])):
        print("Invalid component id!")
        return 1
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    global client
    client = mqtt.Client(client_id=component_id, clean_session=False, userdata=None, protocol=4,)
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe
    client.user_data_set({"subscribed_topic": topic})
    client.connect(broker_address, broker_port, 60)
    client_component_ids[client] = component_id
    return client


def renew(component_id: str):
    client.reinitialise(client_id=component_id, clean_session=False, userdata=None)


def disconnect(component_id):
    if component_id is not None:
        client.disconnect()
    else:
        print("Invalid component ID")


def publish(topic: str, data: str, qos: int):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    if not (is_qos(qos)):
        print("Invalid Qos number!")
        return 1
    client.publish(topic=topic, payload=data, qos=qos, retain=False)


def subscribe(topic: str, qos: int):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    if not (is_qos(qos)):
        print("Invalid Qos number!")
        return 1
    client.subscribe(topic=topic, qos=qos)


def unsubscribe(topic: str):
    if not (is_topic(topic)):
        print("Invalid topic number!")
        return 1
    client.unsubscribe(topic=topic)


def loop(user):
    if user:
        client.loop()





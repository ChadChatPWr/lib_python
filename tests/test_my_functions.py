from mqtt import lib_mqtt
lib_mqtt.connect('1', "i am dead")
lib_mqtt.subscribe("1", 0)
lib_mqtt.publish("1","to jest plik", 0)

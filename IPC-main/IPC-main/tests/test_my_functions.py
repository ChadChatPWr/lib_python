import mqtt
from mqtt import lib_mqtt
lib_mqtt.connect(1,"i am dead")
lib_mqtt.subscribe("dupa",0)
lib_mqtt.publish("dupa","to jest plik",0)

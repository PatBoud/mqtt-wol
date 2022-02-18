#!/usr/bin/python3

# MQTT WOL
# Script qui active des appareils via Wake-On-LAN à la réception d'un message MQTT
#
# PatBoud
# 2022-02-18
#
# Prérequis:
#  - Fichier `secrets.py` que vous devez créer
#  - Librairie [pywakeonlan](https://github.com/remcohaszing/pywakeonlan)


print("--- MQTT-WOL ---")
print("Initialisation...")

# Importation des librairies
import paho.mqtt.client as mqtt
from wakeonlan import send_magic_packet

# Importation des paramètres secrets
import secrets


# Définition des variables
mqttTopic = "wakeonlan/#"


print ("OK")


# Fonctions callback de MQTT

def on_connect(client, userdata, flags, rc):
  print("OK!")
  print("Abonnement au topic " + mqttTopic + " ...")
  client.subscribe(mqttTopic)
  print("OK!")

def on_message(client, userdata, message):
  print("RECU: " + message.topic + " : " + str(message.payload.decode("utf-8")))


print("Connexion au serveur MQTT...")
# Initialisation du client MQTT
client = mqtt.Client()
client.on_message=on_message
client.on_connect=on_connect
client.username_pw_set(secrets.mqttUser, password=secrets.mqttPass)
client.connect(secrets.mqttServer, secrets.mqttPort, 60)


client.loop_forever()


# send_magic_packet('ff.ff.ff.ff.ff.ff')

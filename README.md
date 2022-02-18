# mqtt-wol
### Script qui active des appareils via Wake-On-LAN à la réception d'un message MQTT


#### Prérequis

- Fichier `secrets.py` que vous devez créer
- Librairie [pywakeonlan](https://github.com/remcohaszing/pywakeonlan)


#### Exemple de fichier secrets.py

```
mqttServer = "192.168.1.104"
mqttPort = 1883
mqttUser = "utilisateur"
mqttPass = "motdepasse"
```

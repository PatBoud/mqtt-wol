# mqtt-wol
### Script qui active des appareils via Wake-On-LAN à la réception d'un message MQTT


#### Prérequis

- Fichier `secrets.py` que vous devez créer
- Librairie [awake](https://github.com/cyraxjoe/awake)


#### Exemple de fichier secrets.py

```
mqttServer = "192.168.1.104"
mqttPort = 1883
mqttUser = "utilisateur"
mqttPass = "motdepasse"
macOrdiX = "FF-FF-12-34-56-78"
macOrdiY = "FF-AB-12-55-66-77"
```

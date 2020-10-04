import json
import os

import paho.mqtt.client as mqtt


NAME_MAPPINGS = {
    'Balcony-1': 'a4c13890ef1d',
    'Designer-1': 'a4c138cad1ab',
    'Designer-2': 'a4c138bd8b78',
    'Dev-1': 'a4c13831862e',
    'Dev-2': 'a4c13842d14c',
    'Dev-3': 'a4c138a96910',
    'Front-1': 'a4c138bd6ec8',
    'Front-2': 'a4c138d725a4',
    'Kitchen-1': 'a4c138becafd',
    'Meeting-1': 'a4c138cc77c0',
    'Meeting-2': 'a4c13895b966',
    'Toilet-1': 'a4c1382ad5a6',
    'Toilet-2': 'a4c138309f83',
}


def on_connect(self, client, userdata, rc):
    topic = f'ARTISAN/xiaomi/{NAME_MAPPINGS["Meeting-2"]}/status'
    self.subscribe(topic)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    print(payload)


host = os.environ.get('MQTT_HOST')

client = mqtt.Client('Meeting-1')
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()

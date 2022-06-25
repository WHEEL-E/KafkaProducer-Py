from math import prod
from kafka import KafkaProducer
import json
from FakeSensorData import returnFakeData
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=['192.168.1.115:9092'], value_serializer=json_serializer)


if __name__ == "__main__":
    while 1 == 1:
        sensor_data = returnFakeData()
        print(sensor_data)
        producer.send("TestingTopic", sensor_data)
        time.sleep(1)

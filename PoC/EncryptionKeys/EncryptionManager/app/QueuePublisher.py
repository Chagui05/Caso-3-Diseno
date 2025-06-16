import pika
import os
import json

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'user')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', 'password')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', "46005")
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE', 'kek_email')


def get_rabbitmq_connection():
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
        parameters = pika.ConnectionParameters(host=RABBITMQ_HOST, port=int(RABBITMQ_PORT),
                                               credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        print('connection to RabbitMQ')

    except:
        print("could not connect to RabbitMQ")
        return []

    return [channel, connection]


def declare_objects(channel):
    # Declaramos la cola
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    print("rabbitMQ objects declared")


def publish_message(name, kek, channel):

    message = json.dumps({'name': name,
                          'kek': kek
    })

    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message)

    print(f"message sent: {message}")



def email_notifications(group):

    # Se crea conexion y declara la cola
    rabbitmq_connection = get_rabbitmq_connection()
    declare_objects(rabbitmq_connection[0])

    for elem in group:
        publish_message(elem["nombre"], elem["kek"], rabbitmq_connection[0])

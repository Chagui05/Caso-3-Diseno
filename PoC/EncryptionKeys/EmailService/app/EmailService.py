import pika
import os
import json
from SES import sendMail

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

# Used declare rabbitmq queues and exchange
def declare_objects(channel):
    # Declaramos la cola
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    print("rabbitMQ objects declared")


def callback(channel, method, properties, body):

    data = json.loads(body)
    name = data['name']
    kek = data['kek']

    sendMail(name, kek)


if __name__ == "__main__":

    #Se crean los objetos en rabbitMQ
    channel, connection = get_rabbitmq_connection()
    declare_objects(channel)

    print("Listening...")
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

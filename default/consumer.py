import pika, sys, os


def main():
    # 1. create the connection,
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    # 2. creates a channel
    channel = connection.channel()

    # 3.if the queue does not exists , we can create the queue
    # and associate it with the channel
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print("[x] received %r" % body)

    # 4. associate the callback function with the message queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] waiting for the messages. To exit press Ctrl-C")

    # 5. Start consuming the message
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

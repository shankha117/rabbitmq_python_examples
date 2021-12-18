import pika

# 1. create the connection,
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 2. creates a channel
channel = connection.channel()

# 3. create an exchange define the bindings ;
# since we are crating the default exchange we are not creating the bindings

# 4.if the queue does not exists , we can create the queue
# create a queue through the channel
channel.queue_declare(queue="hello")

# 5.publish the message
# routing_key == queue
channel.basic_publish(exchange="", routing_key="hello", body="hello_world 1")
print("[x] Sent Hello World")

# 6. close the connection
connection.close()

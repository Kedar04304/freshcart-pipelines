import json
import sys
import time
import pika

zone = sys.argv[1] if len(sys.argv) > 1 else "north"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.exchange_declare(
    exchange="freshcart_orders",
    exchange_type="topic",
    durable=True
)

queue = f"driver_{zone}"
channel.queue_declare(queue=queue, durable=True)

channel.queue_bind(
    exchange="freshcart_orders",
    queue=queue,
    routing_key=f"orders.{zone}.*"
)

channel.basic_qos(prefetch_count=1)

def process_message(ch, method, properties, body):
    order = json.loads(body)

    print(f"Driver {zone} received:", order)

    if order.get("valid") is True:
        print("ACK: Order accepted")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        print("NACK: Invalid order rejected")
        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False
        )

channel.basic_consume(
    queue=queue,
    on_message_callback=process_message
)

print(f"Driver {zone} waiting for orders for 120 seconds.")

start = time.time()

try:
    while time.time() - start < 120:
        connection.process_data_events(time_limit=1)
finally:
    channel.stop_consuming()
    connection.close()
    print(f"Driver {zone} stopped.")

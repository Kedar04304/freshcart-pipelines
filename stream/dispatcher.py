import json
import time
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.exchange_declare(
    exchange="freshcart_orders",
    exchange_type="topic",
    durable=True
)

orders = [
    {"id": 1, "zone": "north", "priority": "normal", "valid": True},
    {"id": 2, "zone": "south", "priority": "high", "valid": True},
    {"id": 3, "zone": "east", "priority": "normal", "valid": False},
    {"id": 4, "zone": "west", "priority": "high", "valid": True},
    {"id": 5, "zone": "north", "priority": "high", "valid": True},
    {"id": 6, "zone": "south", "priority": "normal", "valid": False},
    {"id": 7, "zone": "east", "priority": "high", "valid": True},
    {"id": 8, "zone": "west", "priority": "normal", "valid": True},
    {"id": 9, "zone": "north", "priority": "normal", "valid": True},
]

for order in orders:
    routing_key = f"orders.{order['zone']}.{order['priority']}"

    channel.basic_publish(
        exchange="freshcart_orders",
        routing_key=routing_key,
        body=json.dumps(order),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print("Published:", routing_key, order)
    time.sleep(1)

connection.close()
print("Dispatcher finished.")

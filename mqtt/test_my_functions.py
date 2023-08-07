import lib_mqtt as ipc
import random
import threading

response_available = threading.Event()  # Create an event to signal response availability
received_content = None  # Initialize received_content variable


def my_on_message(client, userdata, msg):
    print("MyOnMessage")
    global received_content
    received_content = msg.payload.decode()
    print("Received message:", received_content)
    response_available.set()  # Set the event to signal response availability


def wait_for_response():
    while True:
        print("WaitForResponse")
        response_available.wait()  # Wait for the event to be set
        response_available.clear()  # Clear the event for the next response
        process_response()  # Process the response or take actions


def process_response():
    print("ProcessResponse")
    global received_content
    print("Processing response:", received_content)
    received_content = None  # Clear the content after processing


id = '3-' + str(random.randrange(1, 1000))
user = ipc.connect(id, '1')
user.on_message = my_on_message
user.on_subscribe = ipc.on_subscribe
user.on_disconnect = ipc.on_disconnect
ipc.subscribe('1', 0)

# Create a separate thread to wait for responses
response_thread = threading.Thread(target=wait_for_response)
response_thread.start()

while True:
    ipc.loop(user)
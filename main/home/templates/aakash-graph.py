import matplotlib.pyplot as plt
import random
import time
import threading

# Global variables to store data
x_data = []
y_data = []

# Function to update the graph
def update_graph():
    while True:
        x_data.append(time.time())  # x-axis: current timestamp
        y_data.append(random.randint(0, 10))  # y-axis: random values for demonstration
        plt.clf()  # Clear the previous plot
        plt.plot(x_data, y_data, label='Live Data')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.pause(1)  # Pause to update the plot every 1 second

# Create a thread to run the update_graph function in the background
graph_thread = threading.Thread(target=update_graph)
graph_thread.daemon = True
graph_thread.start()

# Display the live graph
plt.ion()  # Turn on interactive mode for live plotting
plt.show()

# Keep the program running
try:
    while True:
        pass
except KeyboardInterrupt:
    plt.ioff()  # Turn off interactive mode when the program is interrupted
    plt.close()

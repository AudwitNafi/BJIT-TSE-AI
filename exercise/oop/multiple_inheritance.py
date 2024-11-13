# Base class for all devices
class Device:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} device initialized.")

# Remote control functionality
class RemoteControl:
    def turn_on(self):
        print(f"{self.name} is now ON remotely.")
        
    def turn_off(self):
        print(f"{self.name} is now OFF remotely.")

# Internet-connected functionality
class InternetConnected:
    def connect_to_internet(self):
        print(f"{self.name} connected to the internet.")
        
    def disconnect_from_internet(self):
        print(f"{self.name} disconnected from the internet.")

# SmartDevice inherits from Device, RemoteControl, and InternetConnected
class SmartDevice(Device, RemoteControl, InternetConnected):
    def __init__(self, name):
        super().__init__(name)  # Initialize Device attributes

# Create a SmartDevice instance
smart_tv = SmartDevice("Smart TV")

# Using methods from both parent classes
smart_tv.turn_on()                # From RemoteControl
smart_tv.connect_to_internet()     # From InternetConnected
smart_tv.disconnect_from_internet()
smart_tv.turn_off()

# remoteControl = RemoteControl()
# remoteControl.turn_off()

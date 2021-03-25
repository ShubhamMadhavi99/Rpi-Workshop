import pyMultiSerial

p = pyMultiSerial.pyMultiSerial()


def authenticate_device(portno,serial):
    
    pass

#Register Callback - authenticate_device will be called whenever a new USB device is found.
p.port_connection_found_callback = authenticate_device


def handle_input(portno,serial,text):
    
    pass

#Register Callback - handle_input will be called whenever data is received from USB device
p.port_read_callback = handle_input






# Start Monitoring Serial Ports
p.Start()
'''
Library pyMultiSerial Functions: 
    1. Scans to check if any new device is connected to USB - port_connection_found_callback(portno,serial)
    2. Checks if any device is sending data through USB port - port_read_callback(portno,serial,text)
    3. Scans too check if any device has been disconnected from USB - port_disconnection_callback(portno)
'''

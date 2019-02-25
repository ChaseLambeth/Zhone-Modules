from netmiko import ConnectHandler

host = input('MXK IP Address: ')
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
print ('Connecting...')

# Connects to the device using the credentials used above.
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
print ('Connected to ' + host + '!')

device.find_prompt()

# Send the "swversion" command
output = device.send_command("swversion")

# Prints output of the "swversion" command.
print (host + ' is currently on:')
print(output)

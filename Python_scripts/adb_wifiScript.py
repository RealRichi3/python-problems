"""
Simple script to connect ADB over wifi for android

Requirements
- USB Debbuging enabled on android device

"""


import os

command  = os.popen('adb shell ip route').read()
myIP = ''.join(list(command)[command.index('src ') + 3:])   # Gets IP Address from windows output
print('Your IP address is: {}'.format(myIP))


command_list = ['adb tcpip 5555','adb connect {}'.format(myIP)]
for command in command_list:
    os.system(command)

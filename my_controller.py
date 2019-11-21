import time 
import serial
import re

class SensorDataController(object):
    '''
    Use the serial interface to receive sensor data from the control system
    '''

    def __init__(self):
        self.usbPort = '/dev/ttyS0'
        self.baud_rate = 9600
        self.running = True
        self.maxValue = 2**12 - 1
        self.throttle = 0
        self.angle = 0
        self.out = (0, 0, 'user', 1)
        self.img = None
        self.ser = serial.Serial(self.usbPort, self.baud_rate)
        self.dataRegex = r"(s|b|a)([0-9]{4})"

    def shutdown(self):
        self.running = False
        time.sleep(0.1)

    def update(self):

        # This sleep is needed because donkeycar is donkey
        time.sleep(2)
        while self.running:

            self.out = self.run(self.img)
            self.throttle = 4095 / self.maxValue
            self.angle = 1.2

    def run_threaded(self, img):
        self.img = img
        return self.out

    def run(self, img):
        try:
            if self.ser.in_waiting > 0:
                msg = self.ser.readline().decode()
                matches = re.finditer(self.dataRegex, msg, re.MULTILINE)

                for matchNum, match in enumerate(matches):
                    
                    valueType = match.group(1)
                    value = float(match.group(2)) / self.maxValue

                    if valueType == 'a':
                        self.throttle = value
                    elif valueType == 's':
                        if value < .5:
                            self.angle = (2 * value) - 1
                        else:
                            self.angle = 2 * (value - .5)
                    #elif valueType == 'b':
                
        # serial.SerialException is thrown when there is no data, so just keep trying to read it.
        except TypeError as e:
            self.ser.close()
            print('Serial connection with main control system was disconnected, shutting the system down')
            # TODO: Set the autonomous_system pin to LOW
            exit(1)
        except Exception as e1:
            print(e1)
            pass
        return self.throttle, self.angle, 'user', 1

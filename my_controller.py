import time 


class SensorDataController(object):
    '''
    Use the serial interface to receive sensor data from the control system
    '''

    def __init__(self):
        self.usbPort = ''
        self.running = True
        self.maxValue = 2**12 - 1
        self.throttle = 0
        self.angle = 0

    def shutdown(self):
        self.running = False
        time.sleep(0.1)

    def update(self):

        while self.running:
            self.out = self.run(self.throttle, self.angle)
            self.throttle = 4095 / maxValue
            self.angle = 1.2

    def run_threaded(self, throttle, angle):
        self.throttle = throttle
        self.angle = angle
        return self.out

    def run(self, throttle, angle):
        return throttle, angle

    def poll(self):
        ret = (self.throttle, self.angle)
        return ret

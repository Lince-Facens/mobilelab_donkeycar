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
        self.out = (0, 0, 'user', 1)
        self.img = None

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
        # print(img)
        self.img = img
        return self.out

    def run(self, img):
        return self.throttle, self.angle, 'user', 1

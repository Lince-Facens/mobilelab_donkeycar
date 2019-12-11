class PWMThrottle:
    """ 
    Wrapper over a PWM motor cotnroller to convert -1 to 1 throttle
    values to PWM pulses.
    """
    MIN_THROTTLE = -1
    MAX_THROTTLE =  1

    def __init__(self, controller=None,
                       max_pulse=300,
                       min_pulse=490,
                       zero_pulse=350):

        self.controller = controller
        self.max_pulse = max_pulse
        self.min_pulse = min_pulse
        self.zero_pulse = zero_pulse
    
        time.sleep(1)

    def run(self, throttle):
        if throttle > 0:
            pulse = dk.utils.map_range(throttle,
                                    0, self.MAX_THROTTLE, 
                                    self.zero_pulse, self.max_pulse)
        else:
            pulse = dk.utils.map_range(throttle,
                                    self.MIN_THROTTLE, 0,  
                                    self.min_pulse, self.zero_pulse)

        self.controller.set_pulse(pulse)
    
    def shutdown(self):
        self.run(0) #stop vehicle


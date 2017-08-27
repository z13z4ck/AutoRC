"""
Python class file to initialize pigpio module for RPI
"""

import pigpio

class rpigpio:
    def __init__(self, _init=None):

        self.servo_pin = 12
        self.throttlepin = 13

        self.pi = pigpio.pi()
        self.pi.set_mode(self.servo_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.throttlepin, pigpio.OUTPUT)

    def write_servo(self, _val=None):
        """
        write servo value using pigpio API
        :param _val:
        :return:
        """
        if not _val:
            print("Please insert value")
            exit()
        self.pi.set_servo_pulsewidth(self.servo_pin, _val*10)

    def write_throttle(self, _val=None):
        if not _val:
            print("Please insert value")
            exit()
        self.pi.set_PWM_dutycycle(self.throttlepin, _val)

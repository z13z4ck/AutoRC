import BlynkLib


class rpi(object):

    def __init__(self):

        BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
        self.blynk = BlynkLib.Blynk(BLYNK_AUTH)

        self.pin0 = None
        self.pin1 = None

        self.blynk.add_virtual_pin(0, write=self.write_pin0)
        self.blynk.add_virtual_pin(1, write=self.write_pin1)
        self.blynk.add_virtual_pin(5, write=self.write_pin5)

        self.blynk.run()

    def write_pin1(self, value):
        self.pin1 = value

    def write_pin0(self, value):
        self.pin0 = value

    def write_pin5(self, value):
        print("Pin0 = ", self.pin0, "\tPin1 = ", self.pin1)


if __name__ == "__main__":
    rasp = rpi()

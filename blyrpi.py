import BlynkLib
from multiprocessing import Pool as threadpool


class Rpi(object):

    def __init__(self, run=None):

        BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
        self.blynk = BlynkLib.Blynk(BLYNK_AUTH)

        self.pin0 = None
        self.pin1 = None
        self.pin2 = None

        self.collectmode = None

        # attach virtual pin handler
        # self.blynk.add_virtual_pin(0, write=self.write_pin0)
        # self.blynk.add_virtual_pin(1, write=self.write_pin1)
        # self.blynk.add_virtual_pin(5, write=self.write_pin5)

        self.blynk.add_virtual_pin(5, write=self.data_collect)  # call for data collection
        self.blynk.add_virtual_pin(1, write=self.write_pin1)
        self.blynk.add_virtual_pin(2, write=self.write_pin2)

        if run:
            self.blynk.run()

    def write_pin1(self, value):
        self.pin1 = value

    def write_pin0(self, value):
        self.pin0 = value

    def write_pin2(self, value):
        self.pin2 = value

    def write_pin5(self, value):
        print("Pin0 = ", self.pin0, "\tPin1 = ", self.pin1)

    def data_collect(self, value):
        """
        Call collect mode for data collection
        :param value: represent pin from Blynk APP
        :return:
        """
        import collect
        self.collectmode = 1
        collect.Collect(_mode='thread')

if __name__ == "__main__":
    rasp = Rpi(run=True)

import BlynkLib

# BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
#
# blynk = BlynkLib.Blynk(BLYNK_AUTH)
#
# pin0 = None
# pin1 = None
# mode = None
#
#
# @blynk.VIRTUAL_WRITE(1)
# def write_pin1(value):
#     global pin1
#     pin1 = value
#
#
# @blynk.VIRTUAL_WRITE(0)
# def write_pin0(value):
#     global pin0
#     pin0 = value
#
# @blynk.VIRTUAL_WRITE(5)
# def write_pin5(value):
#     # print("Pin0 = ", pin0, "\tPin1 = ", pin1)
#     global mode
#     mode = value
#
#
# blynk.run()




class rpi(object):


    # BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
    # blynk = BlynkLib.Blynk(BLYNK_AUTH)

    def __init__(self):
        BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
        self.blynk = BlynkLib.Blynk(BLYNK_AUTH)

        self.pin0 = None
        self.pin1 = None

        self.blynk.add_virtual_pin(0, write=self.write_pin0())
        self.blynk.add_virtual_pin(1, write=self.write_pin1())
        self.blynk.add_virtual_pin(5, write=self.write_pin5())

        self.blynk.run()

    # @blynk.VIRTUAL_WRITE(1)
    def write_pin1(self, value):
        self.pin1 = value

    # @blynk.VIRTUAL_WRITE(0)
    def write_pin0(self, value):
        self.pin0 = value

    # @blynk.VIRTUAL_WRITE(5)
    def write_pin5(self, value):
        print("Pin0 = ", self.pin0, "\tPin1 = ", self.pin1)

    # def run(self, func=blynk):
    #     func.run()


if __name__ == "__main__":
    rasp = rpi()

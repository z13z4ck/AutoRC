import BlynkLib
#
# BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
#
# blynk = BlynkLib.Blynk(BLYNK_AUTH)
#
# pin0 = None
# pin1 = None
#
#
# @blynk.VIRTUAL_WRITE(1)
# def write_pin1(value):
#     pin1 = value
#
#
# @blynk.VIRTUAL_WRITE(0)
# def write_pin0(value):
#     pin0 = value
#
# @blynk.VIRTUAL_WRITE(5)
# def write_pin5(value):
#     print("Pin0 = ", pin0, "\tPin1 = ", pin1)
#
#
#
#
#
# blynk.run()


class rpi():

    BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
    blynk = BlynkLib.Blynk(BLYNK_AUTH)


    def __init__(self):
        # BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'
        # self.blynk = BlynkLib.Blynk(BLYNK_AUTH)

        self.pin0 = None
        self.pin1 = None

    @blynk.VIRTUAL_WRITE(1)
    def write_pin1(self, value):
        self.pin1 = value

    @blynk.VIRTUAL_WRITE(0)
    def write_pin0(self, value):
        self.pin0 = value

    @blynk.VIRTUAL_WRITE(5)
    def write_pin5(self, value):
        print("Pin0 = ", self.pin0, "\tPin1 = ", self.pin1)

    def run(self, func=blynk):
        func.run()


if __name__ == "__main__":
    
    rpi()

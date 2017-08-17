import BlynkLib

BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'

blynk = BlynkLib.Blynk(BLYNK_AUTH)

pin0 = None
pin1 = None


@blynk.VIRTUAL_WRITE(1)
def write_pin1(value):
    pin1 = value


@blynk.VIRTUAL_WRITE(0)
def write_pin0(value):
    pin0 = value

@blynk.VIRTUAL_WRITE(5)
def write_pin5(value):
    print("Pin0 = ", pin0, "\tPin1 = ", pin1)





blynk.run()

import BlynkLib

BLYNK_AUTH = '60c5c89c4cb243428d02140bdaf4f896'

blynk = BlynkLib.Blynk(BLYNK_AUTH)




@blynk.VIRTUAL_READ(1)
def write_handle(value):
    print('Current V1 Value: {}'.format(value))


blynk.run()

import cv2
import os
import time
import json
import numpy as np
# from __builtin__ import raw_input

from suiron.core.SuironIO import SuironIO


# TODO: add threading
# TODO: use class

class collect:
    def __init__(self, _mode=None):
        pass


    def main(self):
        # Load image settings
        with open('settings.json') as d:
            SETTINGS = json.load(d)

        # Instantiatees our IO class
        suironio = SuironIO(width=SETTINGS['width'], height=SETTINGS['height'], depth=SETTINGS['depth'])
        suironio.init_saving()

        # Allows time for the camerae to warm up
        print('Warming up...')
        time.sleep(5)

        raw_input('Press any key to conitnue')
        print('Recording data...')
        while True:
            try:
                suironio.record_inputs()
            except KeyboardInterrupt:
                break

        print('Saving file...')
        suironio.save_inputs()


if __name__ == "__main__":
    collect.main()

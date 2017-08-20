import cv2
import os
import time
import json
import numpy as np
from multiprocessing import Pool as threadpool
from threading import Thread
# from __builtin__ import raw_input

from suiron.core.SuironIO import SuironIO


class Collect:
    def __init__(self, _mode=None):
        if _mode == 'thread':
            # self.pool = threadpool(3)
            # self.output = self.pool.map(self.main)
            self.output = Thread(target=self.main)
            self.output.start()

    def main(self):
        # Load image settings
        with open('settings.json') as d:
            SETTINGS = json.load(d)

        # Instantiates our IO class
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
        self.stoppool()

    def stoppool(self):
        # self.pool.close()
        # self.pool.join()
        self.output.join()
        pass


if __name__ == "__main__":
    Collect.main()

"""
FIle to control mode transition
"""


class mode:
    def __init__(self):
        pass

    def collect(self, _mode):
        pass

    def train(self):
        pass

    def auto(self):
        pass


if __name__ == "__main__":
    _mode = mode()
    print('Please enter the mode that you wish to run')
    print('1. collect Mode')
    print('2. AutoMode')
    _task = input('(1/2) --->') or None

    if not _task:
        exit()

    if _task == '1':
        _mode.collect(_mode='thread')

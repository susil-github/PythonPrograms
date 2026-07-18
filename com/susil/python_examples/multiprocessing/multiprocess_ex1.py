from multiprocessing import Process
import os

def show():
    print('Hi this is susil and am a  developer')

if __name__ == '__main__':
    p1 = Process(target=show())
    p1.start()
    p1.join()

import pandas as pd
class GROOutput():
    def __init__(self):
        pass

    def format(self,data):
        #print("{0[0]:>9s}{0[1]:>6s}{0[2]:5d}{0[3]:8.3f}{0[4]:8.3f}{0[5]:8.3f}{0[6]:8.4f}{0[7]:8.4f}{0[8]:8.4f}".format(data))
        with open("test.dat", mode='w') as f:
            f.writelines("{0[0]:>9s}{0[1]:>6s}{0[2]:5d}{0[3]:8.3f}{0[4]:8.3f}{0[5]:8.3f}{0[6]:8.4f}{0[7]:8.4f}{0[8]:8.4f}".format(data))

if __name__ == "__main__":
    grodata=["268PPPm", "C1", 4820, 5.575, 3.053, 5.478, 0.1296, 0.0300, 0.4972]
    GRO = GROOutput()
    GRO.format(grodata)

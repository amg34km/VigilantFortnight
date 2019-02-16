class DataSentence():
    def __init__(self):
        self.sentence = ''
    def addNumdata(self, dataname, numdata):
        # dataname : number
        self.sentence = "{}{} : {}\n".format(self.sentence, dataname, str(numdata))
        #print(self.sentence)

    def addListdata(self, dataname, listdata):
        # dataname : list
        self.sentence = "{}{} : {}\n".format(self.sentence, dataname, ' '.join(map(str,listdata)))
        #print(self.sentence)

    def addSentence(self, string):
        self.sentence = "{}{}\n".format(self.sentence, string)

    def rerturnSentence(self):
        return self.sentence

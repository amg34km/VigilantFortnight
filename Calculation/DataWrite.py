class DataSentence():
    def __init__(self):
        self.sentence = ''
    def dataname_and_numdata(self, dataname, numdata):
        #self.sentence = dataname + " : " + str(numdata) + "\n"
        "{}{} : {}\n".format(self.sentence, dataname, numdata)
    def dataname_and_list(self, dataname, listdata):
        #self.sentence = dataname + " : " + ' '.join(map(str,listdata)) + "\n"

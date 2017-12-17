class SMFRecordBuilder:
    smfrecord = None

    def getrecord(self):
        return self.smfrecord

    def startrecord(self, firstsegment):
        raise NotImplementedError

    def addsegment(self, segment):
        raise NotImplementedError




class NonSPannedRecordBuilder(SMFRecordBuilder):
    def startrecord(self,firstsegment):
        self.smfrecord = firstsegment

    def addsegment(self, segment):
        self.smfrecord += segment[4:]

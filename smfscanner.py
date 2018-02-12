import binascii
import codecs
import smfutils
import smfrecordbuilder
import smfrecordmanager


class SMFfileScanner:

    def __init__(self, recordbuilder, recordmanager):
        self.recordbuilder = recordbuilder
        self.recordmanager = recordmanager

    def parse(self, inputfile):
        with open(inputfile, mode='rb') as file:
            blocklength = int.from_bytes(file.read(2), byteorder='big')
            while file.read(2):
                self.parseblock(file.read(blocklength - 4))
                blocklength = int.from_bytes(file.read(2), byteorder='big')

    def parseblock(self, block):
        bytescounter = 0
        while bytescounter < len(block):
            recordlength, segmentdescriptor = self.parseRDW(
                block[bytescounter:bytescounter + 3])
            self.parserecord(
                block[bytescounter + 0:bytescounter + recordlength],
                segmentdescriptor)
            bytescounter += recordlength

    def parserecord(self, record, segmentdescriptor):
        if segmentdescriptor == 0:
            self.createrecord(record)
        elif segmentdescriptor == 1:
            self.recordbuilder.startrecord(record)
        elif segmentdescriptor == 2:
            self.finishrecord(record)
        elif segmentdescriptor == 3:
            self.recordbuilder.addsegment(record)

    def createrecord(self, record):
        self.recordbuilder.startrecord(record)
        self.recordmanager.managerecord(self.recordbuilder.getrecord())

    def finishrecord(self, record):
        self.recordbuilder.addsegment(record)
        self.recordmanager.managerecord(self.recordbuilder.getrecord())

    def parseRDW(self, bytesrdw):
        return int.from_bytes(bytesrdw[0:2],byteorder='big') , int.from_bytes(bytesrdw[2:3],byteorder='big')


builder = smfrecordbuilder.NonSPannedRecordBuilder()
manager = smfrecordmanager.TransformerRecordManager()
assembler = SMFfileScanner(builder, manager)
assembler.parse("smf.gsy7.smfaltro.d171122.t220835")

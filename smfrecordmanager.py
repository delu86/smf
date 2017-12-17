import binascii
import codecs
import smfutils

class SMFRecordManager:


    def managerecord(self, smfrecord):
        raise NotImplementedError


class InfoSMFRecordManager(SMFRecordManager):
    
    def managerecord(self, smfrecord):
        recordType = recType = int.from_bytes(smfrecord[5:6], byteorder='big')
        systemID = codecs.decode(smfrecord[14:18], "cp500")
        time = smfrecord[6:10]
        c, y1, y2, d1, d2, d3 = smfutils.getsmfdate(smfrecord[10:14])
        date = smfutils.convertsmfdate(c, y1, y2, d1, d2, d3)
        print(" ", "Type:", recordType, "System:", systemID, "Date:", date,
              len(smfrecord))

import binascii
import codecs
import smfutils
import smfreader

class SMFReaderFactory:
    @staticmethod
    def get_reader(recordtype):
        if(recordtype==30):
            return smfreader.SMF030Reader()
        else:
            return None



class SMFRecordManager:


    def managerecord(self, smfrecord,output=None):
        raise NotImplementedError

    def _get_record_type(self,smfrecord):
        return int.from_bytes(smfrecord[5:6], byteorder='big')


class InfoSMFRecordManager(SMFRecordManager):

    def managerecord(self, smfrecord):
        recordType  = int.from_bytes(smfrecord[5:6], byteorder='big')
        systemID = codecs.decode(smfrecord[14:18], "cp500")
        time = smfrecord[6:10]
        c, y1, y2, d1, d2, d3 = smfutils.getsmfdate(smfrecord[10:14])
        date = smfutils.convertsmfdate(c, y1, y2, d1, d2, d3)
        print(" ", "Type:", recordType, "System:", systemID, "Date:", date,
              len(smfrecord))

class TransformerRecordManager(SMFRecordManager):

    def managerecord(self, smfrecord, output='json'):
        smfrecord_type = self._get_record_type(smfrecord)
        reader = SMFReaderFactory.get_reader(smfrecord_type)
        if(reader!=None):
            record_obj = reader.read(smfrecord)
            


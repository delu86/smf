import binascii
import codecs
import datetime

def  cyydddF(bytes) :
    c = 20 if bytes[0] & 0b1111 else 19
    y1= bytes[1] >> 4
    y2= bytes[1] & 0b1111
    year = 20*100+ y1*10 + y2
    dateBase = datetime.date(year,1,1)
    d1= bytes[2] >> 4
    d2= bytes[2] & 0b1111
    d3= bytes[3] >> 4
    dayOfyear = d1*100+d2*10+d3 -1
    finalDate = dateBase + datetime.timedelta(days=dayOfyear)
    return finalDate



    
with open('smf.gsy7.smfaltro.d171122.t220835', mode='rb') as file: 
    blockLength = int.from_bytes(file.read(2),byteorder='big')
    while file.read(2) :
        block = file.read(blockLength -4)
        counter = 0
        while counter < blockLength-4:
            recordLength = int.from_bytes(block[counter:counter+2],byteorder='big')
            segmentDesc1 = int.from_bytes(block[counter+2:counter+3],byteorder='big')
            if (segmentDesc1 == 0) or (segmentDesc1 == 1 ) :
                segmentDesc2 = int.from_bytes(block[counter+3:counter+4],byteorder='big')
                flag = int.from_bytes(block[counter+4:counter+5],byteorder='big')
                recType = int.from_bytes(block[counter+5:counter+6],byteorder='big')
                time = block[counter+6:counter+10]
                print(counter)
                date = cyydddF(block[counter+10:counter+14])
                systemID = codecs.decode(block[counter+14:counter+18] , "cp500");
                print(" ",recordLength, segmentDesc1, recType,date,systemID)
            counter = counter+recordLength
        blockLength = int.from_bytes(file.read(2),byteorder='big')

   

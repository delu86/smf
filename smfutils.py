import datetime

#GET SMF DATE FROM BYTES . The date is in packed format
def getsmfdate(bytes):
    c = 20 if bytes[0] & 0b1111 else 19
    y1 = bytes[1] >> 4
    y2 = bytes[1] & 0b1111
    d1 = bytes[2] >> 4
    d2 = bytes[2] & 0b1111
    d3 = bytes[3] >> 4
    return c,y1,y2,d1,d2,d3
    
def convertsmfdate(c,y1 ,y2 ,d1 ,d2, d3):
    year = 20*100+ y1*10 + y2
    dayOfyear = d1*100+d2*10+d3 -1
    return datetime.date(year,1,1) + datetime.timedelta(days=dayOfyear)


def timefrommidnight(hundredsofsecond):
    return true



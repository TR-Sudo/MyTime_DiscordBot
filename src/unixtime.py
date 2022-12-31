import time

def conToUnixTime(prevTime):
    prevTime=prevTime.upper()
    tme,yr,mth,day=prevTime.split("/")
    hr,min=to24Hr(tme)
    return time.mktime((int(yr), int(mth), int(day), hr, min, 0, 0, 0, 0))

def con12TimeToUnix(prevTime):
    prevTime=prevTime.upper()
    hr,min=to24Hr(prevTime)
    return time.mktime((2023,1,1,hr,min, 0, 0, 0, 0))

def to24Hr(tme):
    if "PM" in tme:
        tme=tme.replace("PM","")
        hr,min=tme.split(":")
        hr=int(hr)
        min=int(min)
        if hr>=1 and hr<12:
            hr=12+hr
    
    if "AM" in tme:
        tme=tme.replace("AM","")
        hr,min=tme.split(":")
        hr=int(hr)
        min=int(min)
        if hr==12:
            hr=hr-12
    return [hr,min]
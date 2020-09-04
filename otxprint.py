import re
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from collections import defaultdict

otx = OTXv2("39cf879fe132e36e50547ea5d9fe5911c3ce099d4ef7680a42c29cf84153a740")
otxlist = []

#Create regular expressions to pick out specific types of IOCs from the list
URL = re.compile(r'^([a-zA-Z0-9\-\.]+\.[a-zA-Z]+)$')
MD5 = re.compile(r'^([a-z0-9]{32})$')
SHA256 = re.compile(r'^([a-z0-9]{64})$')
IP = re.compile(r'^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$')

# Get all the indicators associated with a pulse
def getIndicators(pulse_id):
    indicators = otx.get_pulse_indicators(pulse_id)
    for indicator in indicators:
        print(indicator["indicator"])
    
def getIndicatorsfromList(otxIDlist):
    IOCs = {}
    IOCs['IPs'] = []
    IOCs['URLs'] = []
    IOCs['SHAs'] = []
    IOCs['MD5s'] = []
    
    for pulse_id in otxIDlist:
    
        indicators = otx.get_pulse_indicators(pulse_id)
        
        for indicator in indicators:
            #check to see if the IOC matches the format of the IOC and if they do, will be appended to the appropriate list
                                                        
            if URL.match(indicator["indicator"]): 
                IOCs['URLs'].append(indicator["indicator"])
            elif IP.match(indicator["indicator"]):
                IOCs['IPs'].append(indicator["indicator"])
            elif SHA256.match(indicator["indicator"]): #Check if it matches the format of an SHA256 hash and is not a duplicate
                IOCs['SHAs'].append(indicator["indicator"])
            elif MD5.match(indicator["indicator"]): #Check if it matches the format of an MD5 Hash and is not a duplicate
                IOCs['MD5s'].append(indicator["indicator"])
    
    return IOCs

def printIOCs(IOCs):

    for x in IOCs:
        print("%s:" %x)
        for items in IOCs[x]:
            print(items , sep='\n')
        print("\n")
        
if __name__ == "__main__":
    import sys
    IOCList = getIndicatorsfromList(otxlist)
    printIOCs(IOCList)
    #printListToFile(str(sys.argv[1]))
    

#!/usr/bin/python

import re
import otxprint

TicketNum = ""
otxIDList = []
IOCList = {}

def Menu():
    answer = input ("Enter OTX pulse list filename or enter \"input\" to manually enter each pulse ID\n")
   
    if answer.lower() == "input":
        pulseInput()
    else:
        pulseInputFile(answer)

def pulseInputFile(filename):
    try:
        fo = open(filename,"r+")
        for line in fo:
            otxIDList.append(line.strip(' \r\n'))
        fo.close()
        
    except IOError:
        print("Error: Cannot locate file in current directory\n")
        Menu()
    
def pulseInput():
    answer = ""
    
    while True :
        print("\n")
        TicketNum = input("Enter Ticket Number: ")
        print("\n")
        print(TicketNum)
        answer = input("If this is the correct ticket number, enter \"Y\" \n if you want to enter a new ticket number, enter \"N\" ")
        if answer.lower() == "y":
            break 
            
    
    print("\n")
    answer = input("Enter pulse IDs, enter \"Y\" when done\n ")
    
    while True :
        print("\n")
        temp = input("")
        otxlist.append(temp)
        if temp.lower() == "y":
            break 


def IPScriptPrint(IOCs):
    for ip in IOCs['IPs']:
        print("edit \"Malware-"+ip)
        print("set comment "+TicketNum)
        print("set subnet "+ip+" 255.255.255.255")
        print("next\n")
        
def URLScriptPrint(IOCs):
    for ip in IOCs['IPs']:
        print("edit \"Malware-"+ip)
        print("set comment "+TicketNum)
        print("set subnet "+ip+" 255.255.255.255")
        print("next\n")

def getIndicatorsAndPrintScript(otxlist):
    IOCs = otxprint.getIndicatorsfromList(otxlist)
    otxprint.printIOCs(IOCs)
    return IOCs

if __name__ == "__main__":
    import sys
    Menu()
    IOCList = getIndicatorsAndPrintScript(otxIDList)
    
        
    
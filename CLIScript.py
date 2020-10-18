#!/usr/bin/python
#Divyaa Kamalanathan 2020, Intrinium
#Program to extract IOCs from OTX URLs and generate FortiManager CLI script to blacklist IOCs 

import re # Needed for regular expression functions
import otxprint #Used to extract and categorize IOCs from OTX IDs 
from datetime import date  #Used to get the current date 

#Global Vars
TicketNum = "" # Ticket number is added to the notes for each IOC added to the blacklist
CRTicketNum = "" #Change Request Ticket Number is added to the sharepoint blacklist 
otxIDList = [] # An array of OTX IDs to extract IOCs from 
IOCList = {} # The set of IOCs categorized by their types (IPs, URLs, SHA256 hashes, MD5 hashes, Email addresses)
IOCFileName = "OTXiOCs-" + date.today() + ".txt" #The IOC FileName for the day
CLIScriptFileName = "CLIScript-" + date.today() + ".txt" #The CLI Script filename for the day 

#Methods
def Menu(): # First menu, used to get user input on whether they want to input OTX IDs individually or extract from text file containing URLs 
    answer = input ("Enter OTX pulse list filename or enter \"input\" to manually enter each pulse ID\n")
   
    if answer.lower() == "input":
        pulseInput()
    else:
        pulseInputFile(answer)
        
    ticketNumber()

def pulseInputFile(filename): # Opens the file stated by the user and extracts OTX IDs from a list of urls and places them in a list
    try:
        fo = open(filename,"r+")
        for line in fo:
            line = line.strip('https://otx.alienvault.com/pulse/')
            line = line.replace("/","")
            otxIDList.append(line.strip(' \r\n'))
        fo.close()
        
    except IOError:
        print("Error: Cannot locate file in current directory\n")
        Menu()
    
def pulseInput(): #Gets OTX IDs through manual user input
    answer = ""

    while True :
        print("\n")
        temp = input("")
        otxlist.append(temp)
        if temp.lower() == "y":
            break 
            
def ticketNumber(): #Gets the ticket number from user
    while True :
        print("\n")
        TicketNum = input("Enter Ticket Number: ")
        print("\n")
        print(TicketNum)
        answer = input("If this is the correct ticket number, enter \"Y\" \n if you want to enter a new ticket number, enter \"N\" ")
        if answer.lower() == "y":
            break 
            

def CLIScriptPrintToFile(IOCs): #print CLI code to the CLI output file
    fo = open(CLIScriptFileName,"w+")
    fo.write("") #Start script
    for ip in IOCs['IPs']: #Script for IP Blacklisting
        fo.write("edit \"Malware-"+ip)
        fo.write("set comment "+TicketNum)
        fo.write("set subnet "+ip+" 255.255.255.255")
        fo.write("next\n")
        
    for url in IOCs['URLs']: #Script for URL Blacklisting
        fo.write("edit \"Malware-"+ip)
        fo.write("set comment "+TicketNum)
        fo.write("set subnet "+ip+" 255.255.255.255")
        fo.write("next\n")
    fo.write("") #Close Script
    fo.close()

def getIndicatorsAndPrintScript(otxlist): #Gives user option to print extracted files to the screen; prints IOCs to file
    IOCs = otxprint.getIndicatorsfromList(otxlist)
    printToScreen = input("Would you like to print the IOCs to the screen? Y/N")
    if printToScreen.lower == "y":
        otxprint.printIOCs(IOCs)
    iOCOutputFile(IOCFileName,IOCs)
    return IOCs

def iOCOutputFile(filename,iOCList) #Prints IOCs to the file
    try:
        fo = open(filename,"w+")
        for IOCs in iOCList:
            fo.write(IOCs)
        fo.close()
        
    except IOError:
        print("Error")

def updateSharepoint(): #Updates the sharepoint IOC Bans Excel file

def CLIScriptGeneration(): # Full Script Generation Process 



if __name__ == "__main__":
    import sys
    Menu()
    IOCList = getIndicatorsAndPrintScript(otxIDList)
        
    

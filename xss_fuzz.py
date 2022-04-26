import smtplib, requests, sys, os
from optparse import OptionParser
from xml.dom.minidom import parseString

## Global variables
#  ha.ckers.org XSS list
XSSURL        = "http://htmlpurifier.org/live/smoketests/xssAttacks.xml"
DEFAULT_XML   = "./xssAttacks.xml"

# Armazena payloads XSS
def fetchXML():
    """ Connect to  and download XSS cheetsheet"""
    print "[+] Fetching last XSS cheetsheet from ha.ckers.org ..."
    response = requests.get(url=XSSURL)
    xmldata  = response.text
    return xmldata

def parseXML(xmldata):
    """ Parses XML fetched from ha.ckers.org and returns two
        nice py lists for further processing """
    pydata = parseString(xmldata)
    names  = pydata.getElementsByTagName("name")
    codes  = pydata.getElementsByTagName("code")
    return names, codes

def show_payloads():
        xmldata = fetchXML()
        names, codes = parseXML(xmldata)[0], parseXML(xmldata)[1]    
        #showXSSPaylods(names,codes)
        names_f=[]
        codes_f=[]
        for i in range(len(codes)):
            name = getTextFromXML(names[i])
            code = getTextFromXML(codes[i])
            names_f.append(name)
            codes_f.append(code)
        return names_f,codes_f

def getTextFromXML(node):
    """ Returns text within an XML node """ 
    nodelist = node.childNodes
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def showXSSPaylods(names, codes):
    for name, code in zip( names, codes ):
        print "[$] Payload %d  : %s" %\
            (names.index(name), getTextFromXML(name))

if __name__ == '__main__':
    #show_payloads()
    names,codes=show_payloads()
    for i in range(len(names)):
        print names[i]," : ",codes[i]
    
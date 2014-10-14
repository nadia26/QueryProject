from collections import Counter

import re

def readText(filename):
	# reads a file and returns it as a string of content
	instream = open(filename,'r')
	text = instream.read().replace("\n"," ").replace("\r"," ")
	instream.close()
	return text




def makeList(filename):
        # turns the raw census databases of names into lists
	instream = open(filename,'r')
	fulllist = instream.read().replace("\n"," ").split()
	instream.close()
	return [fulllist[x] for x in range(len(fulllist)) if x%4==0]

def findPossibleNames(filetext):
        possiblenames = []
        # uses a regular expression to find groups of 2 or 3 consecutive words all beginning with caps
        for m in re.finditer(r"(([A-Z][a-z-]+){1,2}\s){2,3}", filetext):
                possiblename = ( '%02d-%02d: %s' % (m.start(), m.end(), m.group(0)) )
                if possiblename[-1] == " ": # gets rid of trailing whitespace
                        possiblename = possiblename[:-1]
                        possiblenames.append(possiblename)
        return possiblenames
        
def filterNames (possiblenames, firsts, lasts):
        justthenames = [x[x.find(":")+2:] for x in possiblenames]
        # the list of names that doesn't include the location marker



        return [x for x in justthenames if nameCheck(x, firsts , lasts)]

def nameCheck(fullname,validfirsts,validlasts):
        nameparts = fullname.upper().replace("-"," ").split(" ")

        if len(nameparts)==2:
                return nameparts[0] in validfirsts and nameparts[1] in validlasts
        elif len(nameparts) == 3:
                a = nameparts[0] in validfirsts
                b = (nameparts[1] in validfirsts) or (nameparts[1] in validlasts)
                c = nameparts[2] in validlasts
                return a and (b or c)
                # a must be true to prevent words like "Is" and "By" from getting through


def findNames(text, firsts, lasts):
        possiblenames = findPossibleNames(text)
        return filterNames(possiblenames, firsts, lasts)

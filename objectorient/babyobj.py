#!/usr/bin/python -tt

import urllib
import re
import sys

class BabyNames:
    def __init__(self, year):
        self.year = year
        
    def retrieveNames(self, url):
        #create a method to retrieve the names
        #self.names = result
        
        text = urllib.urlopen(url)  ## get file-like object for url
        year = re.findall(r"-(\d+)", url)
        print year[0]
        if text.info().gettype() == 'text/html':
            if(int(year[0]) < 2011):
                names = re.findall(r"<ol>(.*?)</ol>", text.read())
                for name in names:
                    if re.match(r"<li><a href=\"/.*?\"", name):
                        n = re.findall(r"<li><a href=\".*?\">(.*?)</a>", name)
                    elif re.match(r"<li> <a href=\"/.*?\"", name):
                        n = re.findall(r"<li> <a href=\".*?\">(.*?)</a>", name)
                    else:
                        n = re.findall(r"<li>(.*?)</li>", name)
                    print n
                    
            elif((int(year[0]) == 2016) or (int(year[0]) == 2014)):
                names = re.findall(r"<div class=\"row\"><ol class=\"rankingList small-12 medium-5 large-5 columns\">(.*?)</ol>", text.read())
                for name in names:
                    if re.match(r"<li> <a href=\"/.*?\"", name):
                        n = re.findall(r"<li> <a href=\".*?\">(.*?)</a>.*?</li>", name)
                        print n
                        
            elif(int(year[0]) == 2017):
                names = re.findall(r"<div class=\"row\"><ol class=\"rankingList small-12 medium-5 large-5 columns\">(.*?)</ol>", text.read())
                #print names
                for name in names:
                    if re.match(r"<li> <a href=\"/.*?\"", name):
                        n = re.findall(r"<li> <a href=\".*?\">(.*?)</a>", name)
                        print n
    def printNames(self):
        print "print"
        #print self.names
        #iterate through self.names and print list(dictionary)


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] URL'
        sys.exit(1)
        
    if args[0] == '--summaryfile':
        del args[0]
        
    try:
        text = urllib.urlopen(args[0])  ## get file-like object for url
        if text.info().gettype() == 'text/html':
            uls = re.findall(r"\d+ to \d+</h2><ul>(.*?)</ul>", text.read())
            yearURLs = []
            for ul in uls:
                #extract URL from the <li> tag and add URL to list yearURLs
                urls = re.findall(r"<li><a href=\"/(.*?)\"", ul)
                for each in urls:
                    each = "https://www.babycentre.co.uk/" + each
                    yearURLs.append(each)
                    
            #instantiate my objects for getting baby names
            # we iterate through the list of URLs from above
            for yearURL in yearURLs:
                bn = BabyNames(yearURL)
                bn.retrieveNames(yearURL)
                #bn.printNames()
                
                
    except IOError:
        print "Could not access web address", args[0]
        
    
    
if __name__ == '__main__':
  main()
    
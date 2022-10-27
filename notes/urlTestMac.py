#url test - open a web page for examination

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse
import webbrowser
import os

class URLReader:
    '''Class to read and process a URL'''
    def __init__(self, urlString):
        '''set the URL of interest'''
        self.url = urlString

        #for macs let's also establish web browser location
        self.browserLoc = self.findBrowser()
        #edit the following line to be the absolute location of your browser on your
        #computer if self.findBrowser() does not work properly
        #NOTE: self.findBrowser() only supports chrome, firefox, and safari in the standard mac apps folder

        #for most mac users, you will use one of the following:
        #self.browserLoc = "/Applications/Safari.app"
        #self.browserLoc = "/Applications/Firefox.app"
        #self.browserLoc = "/Applications/Google\ Chrome.app"

        self.client = webbrowser.get("open -a " + self.browserLoc + " %s")
        
    def findBrowser(self):
        firefox = "Firefox.app"
        chrome = "Google Chrome.app"
        chromeFormatted = "Google\ Chrome.app"
        safari = "Safari.app"
        apps = "/Applications"
        div = "/"

        files = os.listdir(apps)
        if chrome in files:
            return apps + div + chromeFormatted
        elif firefox in files:
            return apps + div + firefox
        else:
            return apps + div + safari

    def saveURL(self, fileName):
        '''save the html of the web page to a text file for later processing'''
        urlretrieve(self.url, fileName)
        #here, the urlparse method returns a tuple that splits up the url into components
        print ('The protocol is', urlparse(self.url)[0])
        print ('The net locator is', urlparse(self.url)[1])
        print ('The path is', urlparse(self.url)[2])

    def openURL(self):
        '''extract the title of the web page, printing it and creating an instance variable to hold it'''
        urlFile = urlopen(self.url)
        #now you have a pointer to a file -- it can be used just like a regular infile variable
        #in the sense that it has the same .read(), .readline(), and .readlines() methods
        webpagecode = str(urlFile.read())
        print(webpagecode)
        titlePos = webpagecode.find("<title>")
        titleEnd = webpagecode.find("</title>")
        print(titlePos)
        self.title = webpagecode[titlePos+7:titleEnd]
        print(self.title)
        print (urlFile.geturl())  #shows that you can also get the URL of the file
        ## your code for part 2 goes here ##
        urlFile.close()
    
def main():
    #testing out the URLReader class we defined above
    myUrl=URLReader('http://cs.conncoll.edu/')
    myUrl=URLReader('http://www.xkcd.com/664/')  #go here for a funny comic =)
    #myUrl.saveURL('urlTestfile.txt')
    myUrl.openURL()
    
main()

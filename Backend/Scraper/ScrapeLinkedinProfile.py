'''

Make a class that takes in a URL as the argument and returns key things from a persons linkedin profile

'''
import requests
from LinkedinProfileProxyCurl import LinkedinProfileProxyCurlClass

class ScrapeLinkedinProfileClass:
    def __init__(self, linkedinUrl='https://www.google.com'):
        self.linkedinUrl = linkedinUrl # The input URL
        self.htmlBody = None


    def __repr__(self):
        return f"""
        URL to scrape >> {self.linkedinUrl}
        html body >> {self.linkedinUrl}
        """
    
    def setLinkedinUrl(self, linkedinUrl):
        self.linkedinUrl = linkedinUrl
        return 'Linkedin URL is set' # Adding debugging text to statement so printing set returns the status
    
    def outputProxyLinkedinProfile(self, outputFile='outputProxyCurlSimer.json'):
        # Set path to return to Backend folder
        outputFile = 'Backend/'+ outputFile

        # Send the request using proxy curl class
        linkedinProfileResponseObject = LinkedinProfileProxyCurlClass()
        response = linkedinProfileResponseObject.getLinkedinHTMLResponse()

        # Return without trying to parse HTML to json
        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(response.text)

        return (f"HTML document saved to {outputFile}") # Print this statement to help with debugging

if __name__ == '__main__':
    scraperObject = ScrapeLinkedinProfileClass() # 'https://www.linkedin.com/in/aidan-gorny'
    scraperObject.outputProxyLinkedinProfile()
    print(scraperObject)
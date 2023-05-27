'''

Make a class that takes in a URL as the argument and returns key things from a persons linkedin profile

'''
from bs4 import BeautifulSoup
import lxml
import requests
import os

class ScrapeLinkedinProfileClass:
    def __init__(self, linkedinUrl='https://www.google.com'):
        self.linkedinUrl = linkedinUrl # The input URL
        self.htmlBody = None


    def __repr__(self):
        return f"""URL to scrape >> {self.linkedinUrl}
                html body >> {self.linkedinUrl}
                """
    
    def setLinkedinUrl(self, linkedinUrl):
        self.linkedinUrl = linkedinUrl
        return 'Linkedin URL is set' # Adding debugging text to statement so printing set returns the status
    
    def outputLinkedinProfile(self, outputFile='output.html'):
        # Send a get request to the URL
        outputFile = 'Backend/'+ outputFile
        response = requests.get(self.linkedinUrl)
        response.raise_for_status() # Raise an exception for unseccessful requests

        # Parse the HTML content using Beautiful Soup and lxml
        soup = BeautifulSoup(response.content, 'lxml')

        # Save the output file to output.html
        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

        return (f"HTML document {outputFile} saved to Backend folder.") # Print this statement to help with debugging
    

if __name__ == '__main__':
    scraperObject = ScrapeLinkedinProfileClass() # 'https://www.linkedin.com/in/aidan-gorny'
    print(scraperObject.outputLinkedinProfile())
    print(scraperObject)
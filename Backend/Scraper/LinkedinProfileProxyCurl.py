'''
Class to implement proxy curl API
This give us API calls to pass Linkedin's sign in wall
Documntation on what can be called in the API: https://nubela.co/proxycurl/docs?python#people-api-person-profile-endpoint

Plan is replace with a cheaper proxy solution:
1) Use a proxy service that returns the full html of a linkedin page
    - Will have to build something that posts a request to ignore the blockup
2) Scrape the html from that request using Beautiful Soup and lxml
'''

import requests

class LinkedinProfileProxyCurlClass:
    def __init__(self):
        self.api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        self.api_key = 'Enter API Key'
        self.header_dic = {'Authorization': 'Bearer ' + self.api_key}
        self.params = {
            'url': 'https://www.linkedin.com/in/simerpaulsingh',
            'fallback_to_cache': 'on-error',
            'use_cache': 'if-present',
            'skills': 'include',
        }
        self.response = None

    def __repr__(self):
        return "this works"
    


    def getLinkedinHTMLResponse(self):    
        self.response = requests.get(self.api_endpoint, params=self.params, headers=self.header_dic)
        return self.response


if __name__ == '__main__':
    linkedinProfileObject = LinkedinProfileProxyCurlClass()
    linkedinProfileObject.getProfileData()
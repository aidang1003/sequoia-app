import json

with open('Backend\outputProxyCurl.json', 'r') as file:
        data = json.load(file)

for experience in data['experiences']:
    print(f"Experience >> {experience}\n\n")

# {'starts_at': {'day': 1, 'month': 7, 'year': 2022}, 
#  'ends_at': None, 
#  'company': 'Fast Enterprises, LLC', 
#  'company_linkedin_profile_url': 'https://www.linkedin.com/company/fast-enterprises/', 
#  'title': 'Central Tech Team', 
#  'description': None, 
#  'location': 'Centennial, Colorado, United States', 
#  'logo_url': 'https://s3.us-west-000.backblazeb2.com/proxycurl/company/fast-enterprises/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20230527%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20230527T032820Z&X-Amz-Expires=1800&X-Amz-SignedHeaders=host&X-Amz-Signature=8837ccfe1a6c9725b967c163021c3b41a700180adc077117bf2f0bb32d0abe12'
#  }
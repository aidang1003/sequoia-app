from Backend.Postgres.DatabaseClasses import *
from Backend.Postgres.PostgresFlaskConnection import PostgresFlaskConnectionClass
from requests import request # is this what we need?
from flask import Flask, render_template

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return render_template('index.html', pageTitle='Homepage')  # some basic inline html

@app.route('/recruiter', methods=['GET', 'POST'])
def recruiter():
    global job_position, location, job_description, domain
    if request.method == 'POST':
        user = 'request.json.get'
        if request.headers.get('X-Request-ID') == "User-Input":
            user = 'request.json.get'
            linkedinURL = request.json.get('linkedinURL')
            job_position = request.json.get('jobPosition')
            location = request.json.get('location')
            job_description = request.json.get('jobDescription')
            domain = request.json.get('domain')
            prompt = request.json.get('prompt')
            if location == None:
                location = ""
                print(
                f'job_position: {job_position}, location: {location}, job_description: {job_description}, domain: {domain}')
            item = request.get_json()
            # filterObject = FilterClass(
            #     item, job_position, location, job_description, domain, prompt)
            # file = filterObject.filter()

@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        result = request.json.get('testlinkedinUrl')
        print("URL >> ", result)
    
    return
             

# Run the app.py            
if __name__ == "__main__":
    app.run()
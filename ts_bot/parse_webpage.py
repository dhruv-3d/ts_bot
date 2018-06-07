import webbrowser as wb
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json

class TimeSheetInfo:
    def fetch_project_info():
        s = requests.session()

        ts_url = 'http://192.168.1.201:81/EasyCollab/time_sheets'
        values = {
            '_method': 'POST',
            'data[User][username]': 'dde@narola.email',
            'data[User][password]': 'password'
        }

        r = s.get(ts_url)
        if(r.history):
            print("Request was redirected to: ", r.url)
            ec_req = s.post(r.url, data=values)
            if(ec_req.history):
                print("Again redirected to: ", ec_req.url)
                ts_req = s.get(ts_url)

        soup = BeautifulSoup(ts_req.content,"lxml")

        project_opts = soup.find(id="select-project").find_all('option')

        projects = []
        for i in range(1, len(project_opts)):
            projects.append(project_opts[i].text)

        set_for_resp(projects)

    def set_for_resp(content):
        return content



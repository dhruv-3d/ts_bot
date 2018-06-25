import webbrowser as wb
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json

class TimeSheetInfo(object):
    def __init__(self):
        self.s = requests.session()

    def fetch_project_info(self):

        ts_url = 'http://192.168.1.201:81/EasyCollab/time_sheets'
        values = {
            '_method': 'POST',
            'data[User][username]': 'dde@narola.email',
            'data[User][password]': 'password'
        }

        r = self.s.get(ts_url)
        if(r.history):
            print("Request was redirected to: ", r.url)
            ec_req = self.s.post(r.url, data=values)
            if(ec_req.history):
                print("Again redirected to: ", ec_req.url)
                ts_req = self.s.get(ts_url)

        soup = BeautifulSoup(ts_req.content,"lxml")

        project_opts = soup.find(id="select-project").find_all('option')

        projects = []
        for i in range(1, len(project_opts)):
            projects.append(project_opts[i].text)

        result = self.set_for_resp(projects)

        return result

    def set_for_resp(self, content):
        res = ''
        for pr in content:
            res = res + pr

        print(res)
        return res

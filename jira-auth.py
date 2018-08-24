# make sure you have jira module install
# python -m pip install jira
# this python file cannot name it as jira.py

from jira import JIRA
from jira.exceptions import JIRAError

try:
# jira authentication 
    jira = JIRA('https://yourjira.com', basic_auth=('username','password'))

# The following is optional 
    projects = jira.projects()
    for each_project in projects:
        print(each_project)
except JIRAError as e:
#    print(e.text)
    print(e.status_code)
#    if e.status_code == 401:
#        print('Login failed')

print('done')

from suds.client import Client
from suds import WebFault
from fixture.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost:8888/mantisbt-2.2.1/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client("http://localhost:8888/mantisbt-2.2.1/api/soap/mantisconnect.php?wsdl")
        projects_list = []
        try:
            projects = list(client.service.mc_projects_get_user_accessible(username, password))
            for element in projects:
                projects_list.append(Project(element['name'], element['description']))
            return projects_list
        except:
            return 0


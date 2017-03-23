from model.project import Project
import string
import random
import pytest


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string(15), description=random_string(30))
]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)

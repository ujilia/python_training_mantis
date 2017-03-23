from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="something new", description="something interesting"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)

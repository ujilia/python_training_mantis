from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_projects_page(self):
        wd = self.app.wd
        manage_button = wd.find_elements_by_css_selector('a[href="/mantisbt-2.2.1/manage_overview_page.php"]')[0]
        manage_button.click()
        manage_projects_button = wd.find_element_by_link_text("Manage Projects")
        manage_projects_button.click()

    def open_project_page(self, project=None):
        wd = self.app.wd
        self.open_manage_projects_page()
        if project is not None:
            wd.find_element_by_link_text(project.name).click()
        else:
            projects = wd.find_elements_by_css_selector("table")[0]
            row = projects.find_elements_by_css_selector("tbody tr")[0]
            cell = row.find_elements_by_css_selector("td")[0]
            cell_link = cell.find_element_by_tag_name("a")
            cell_link.click()


    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_projects_page()
            self.project_cache = []
            projects_table = wd.find_elements_by_css_selector("table")[0]
            for element in projects_table.find_elements_by_css_selector("tbody tr"):
                name = element.find_elements_by_css_selector("td")[0].text
                description = element.find_elements_by_css_selector("td")[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_css_selector("input[type='submit']").click()
        self.fill_in_project_form(project)
        wd.find_element_by_css_selector("input[type='submit']").click()
        self.project_cache = None
        # create_button = wd.find_element_by_css_selector('input[type=submit][value="Create New Project"]')
        # create_button.click()

    def fill_in_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page(project)
        delete_button = wd.find_element_by_css_selector('input[type="submit"][value="Delete Project"]')
        delete_button.click()
        delete_button_final = wd.find_element_by_css_selector('input[type="submit"][value="Delete Project"]')
        delete_button_final.click()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        list_count = len(self.get_project_list())
        return list_count

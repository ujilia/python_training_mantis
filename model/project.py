class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def get_name(self):
        return self.name

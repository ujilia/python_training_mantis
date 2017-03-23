from model.project import Project
import string
import random

testdata = [
    Project(name="name", description="description")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

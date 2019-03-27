# Author: Peter
from jinja2 import Template
def index():
    f = open('html/indexjinjia.html')
    result = f.read()
    template = Template(result)
    data = template.render(name='John Doe', user_list=['alex', 'eric'])
    return [data.encode('utf-8')]


def login():
    f = open('login.html')
    data = f.read()
    return [data]
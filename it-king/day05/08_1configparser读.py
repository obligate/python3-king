__author__ = "Peter"

import configparser

conf = configparser.ConfigParser()
conf.read("test_file/example.ini")

print(conf.defaults())
print(conf['bitbucket.org']['user'])
# print(conf.sections())
sec = conf.remove_section('bitbucket.org')
conf.write(open('test_file/example.ini', "w"))

from Rectangle import Rectangle
from Triangle import Triangle
from Ellipse import Ellipse
from utils import file_parser


filetype = raw_input("What file type (json/xml)? ")
filename = raw_input("filename: ")
output = raw_input("output to (f)ile or (s)creen ")

print "Parsing %s into %s" % (filename, filetype)

data = file_parser(filetype, filename)

shape_list = []
for shape in data['shapes']:
    print shape

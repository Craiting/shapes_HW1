from Rectangle import Rectangle
from Triangle import Triangle
from Ellipse import Ellipse
from utils import file_parser, area_organizer


filetype = raw_input("What file type (json/xml)? ")
filename = raw_input("filename: ")

data = file_parser(filetype, filename)
shape_list = []
for shape in data['shapes']:
    if shape['type'] == 'circle' or shape['type'] == 'non-circle':
        shape_list.append(Ellipse(shape['type'], shape['height'], shape['width']))
    elif shape['type'] == 'square'or shape['type'] == 'rectangle':
        shape_list.append(Rectangle(shape['type'], shape['height'], shape['width']))
    elif shape['type'] in ['scalene','isosceles','equillateral']:
        shape_list.append(Triangle(shape['type'], shape['angles'], shape['base'], shape['height']))


area_dict = area_organizer(shape_list)

output = raw_input("output to (f)ile or (s)creen ")
if 's' in output:
    file_exporter('screen', area_dict)
elif 'f' in output:
    file_exporter('file', area_dict)
else:
    print 'invalid destination'

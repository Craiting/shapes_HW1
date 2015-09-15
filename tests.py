import unittest
from Rectangle import Rectangle
from Triangle import Triangle
from Ellipse import Ellipse
from utils import file_parser

class TestParsingMethods(unittest.TestCase):

    def test_json_parse_to_dict(self):
        testjson = 'testjson.json'
        jsontodict = file_parser('json', testjson)
        self.assertEqual(type(jsontodict), type({}))
        self.assertTrue(jsontodict['shapes'][0]['type'] == 'circle')

    def test_xml_parse_to_dict(self):
        testxml = 'testxml.xml'
        xmltodict = file_parser('xml', testxml)
        self.assertEqual(type(xmltodict), type({}))
        self.assertTrue(xmltodict['shapes'][0]['type'] == 'circle')


class TestComputingArea(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle('non-square', 5, 12)
        self.assertEqual(rect.get_area(), 60)

    def test_triangle_area(self):
        triangle = Triangle('scalene',[40,32,98], 3, 8)
        self.assertEqual(triangle.get_area(), 12)

    def test_ellipse_noncircle_area(self):
        ellipse = Ellipse('non-circle',12,4)
        self.assertEqual(round(ellipse.get_area(),1), 37.7)

    def test_ellipse_circle_area(self):
        ellipse = Ellipse('circle',12,12)
        self.assertEqual(round(ellipse.get_area(),1), 113.1)


if __name__ == '__main__':
    unittest.main()

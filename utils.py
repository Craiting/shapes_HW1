import json
import xml.etree.ElementTree as ET
import csv

def file_parser(ftype, name):
    try:
        with open(name) as data_file:
            if(ftype == "json"):
                return json.load(data_file)
            elif(ftype == "xml"):
                e = ET.parse(data_file)
                root = e.getroot()
                shapeDict = {}
                shape_list =[]
                for items in root:
                    for shape in items:
                        tempDict = {}
                        for attr in shape:
                            tempDict[attr.tag] = attr.text
                        shape_list.append(tempDict)
                shapeDict['shapes'] = shape_list
                return shapeDict
            else:
                print "Invalid file type, choose (xml) or (json)"
    except Exception as e:
        print e

def area_organizer(shape_list):
    total_area = 0
    ellipse_area_total = 0
    convexpolygon_area_total = 0
    rectangle_area_total = 0
    triangle_area_total = 0
    circles_area = 0
    non_circles_area = 0
    square_area = 0
    non_square_area = 0
    isosceles_area = 0
    scalene_area = 0
    equillateral_area = 0
    for s in shape_list:
        total_area = total_area + s.get_area()
        if s.name == 'Ellipse': ellipse_area_total = ellipse_area_total + s.get_area()
        if s.name == 'Rectangle': rectangle_area_total = rectangle_area_total + s.get_area()
        if s.name == 'Triangle': triangle_area_total = triangle_area_total + s.get_area()
        if s.kind == 'circle': circles_area = circles_area + s.get_area()
        if s.kind == 'non-circle': non_circles_area = non_circles_area + s.get_area()
        if s.kind == 'square': square_area = square_area + s.get_area()
        if s.kind == 'rectangle': non_square_area = non_square_area + s.get_area()
        if s.kind == 'isosceles': isosceles_area = isosceles_area + s.get_area()
        if s.kind == 'scalene': scalene_area = scalene_area + s.get_area()
        if s.kind == 'equillateral': equillateral_area = equillateral_area + s.get_area()

    convexpolygon_area_total = triangle_area_total + rectangle_area_total
    return {'Ellipses':ellipse_area_total, 'Rectangles':rectangle_area_total,
            'Triangles':triangle_area_total, 'Circles':circles_area,
            'Non-Circles':non_circles_area, 'Squares': square_area,
            'Non-Squares':non_square_area, 'Isosceles': isosceles_area,
            'Scalenes':scalene_area, 'Equillaterals':equillateral_area,
            'ConvexPolygons':convexpolygon_area_total, 'Total': total_area}

def file_exporter(destination, area_dict):
    if destination == 'screen':
        print "Total area of all shapes: \t\t\t %s" % (area_dict['Total'])
        print "\tEllipses: \t\t\t\t  %s" % (area_dict['Ellipses'])
        print "\t\tCircles: \t\t\t  %s" % (area_dict['Circles'])
        print "\t\tNon-circle Ellipses: \t\t  %s" % (area_dict['Non-Circles'])
        print "\tConvex Polygons:\t\t\t  %s" % (area_dict['ConvexPolygons'])
        print "\t\tTriangles: \t\t\t  %s" % (area_dict['Triangles'])
        print "\t\t\tIsosceles: \t\t  %s" % (area_dict['Isosceles'])
        print "\t\t\tScalenes: \t\t  %s" % (area_dict['Scalenes'])
        print "\t\t\tEquillaterals: \t\t  %s" % (area_dict['Equillaterals'])
        print "\t\tRectangles \t\t\t %s" % (area_dict['Rectangles'])
        print "\t\t\tSquares \t\t %s" % (area_dict['Squares'])
        print "\t\t\tNon-Squares \t\t %s" % (area_dict['Non-Squares'])
    elif destination == 'file':
        with open('output.csv', 'wb') as csvfile:
            fwriter = csv.writer(csvfile, delimiter=',')
            fwriter.writerow(['1','','Total area of all Shapes', area_dict['Total']])
            fwriter.writerow(['2','1','Ellipses', area_dict['Ellipses']])
            fwriter.writerow(['3','2','Circles', area_dict['Circles']])
            fwriter.writerow(['4','2','Non-Circle Ellipses', area_dict['Non-Circles']])
            fwriter.writerow(['5','1','Convex Polygons', area_dict['ConvexPolygons']])
            fwriter.writerow(['6','5','Triangles', area_dict['Triangles']])
            fwriter.writerow(['7','6','Isosceles', area_dict['Isosceles']])
            fwriter.writerow(['8','6','Scalene', area_dict['Scalenes']])
            fwriter.writerow(['9','6','Equillaterals', area_dict['Equillaterals']])
            fwriter.writerow(['10','5','Rectangles', area_dict['Rectangles']])
            fwriter.writerow(['11','10','Squares', area_dict['Squares']])
            fwriter.writerow(['12','10','Non-Square Rectangles', area_dict['Non-Squares']])

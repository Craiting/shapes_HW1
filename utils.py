import json


def file_parser(ftype, name):
    if(ftype == "json"):
        try:
            with open(name) as data_file:
                return json.load(data_file)
        except Exception as e:
            print e
    elif(ftype == "xml"):
        print "need to implement xml", name

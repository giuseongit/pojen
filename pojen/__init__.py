import json_parser
import file_handler
import engine
from optparse import OptionParser
import sys

def process_json(jsonpath, outputpath, topclassname, public_fields=False, getset=True):
    to_load = file_handler.read(jsonpath)
    file_handler.create_folder_if_not_exist(outputpath)

    try:
        loaded = json_parser.parse(to_load)
    except ValueError:
        print "not a JSON file (maybe has errors?)"
        exit(-1)

    if len(loaded) == 0:
        print "empty json, exiting"
        exit(-1)

    structure = engine.prepare_structure(loaded, topclassname)
    texts = engine.generate_classes(structure, public_fields, getset)

    for classname, text in texts:
        path = "{}{}{}.java".format(outputpath, file_handler.sep, classname)
        file_handler.save(path, text)

def main():
    parser = OptionParser()
    parser.usage =  "pojen FILENAME [TOPCLASSNAME] [options]\nFILENAME is the path of the input json\n"
    parser.usage += "TOPCLASSNAME is the name of the top class (if any)"
    parser.add_option("-o", "--output-folder", dest="output",
                            help="specify output folder")
    parser.add_option("-p", "--public-fields", dest="public_fields", action="store_true",
                            help="specify if the fileds in the classes must be public")
    parser.add_option("-g", "--get-set", dest="getset", action="store_false",
                            help="specify if the classes must have getters and setters")
    (options, args) = parser.parse_args()

    if len(args) > 2 or len(args) < 1:
        print >>sys.stderr, 'Wrong number of parameters!'
        parser.print_help()
        exit(-1)

    output = options.output if options.output else "output"

    if not file_handler.file_exsits(args[0]):
        print >>sys.stderr, 'File {} does not exists!'.format(args[0])
        exit(-1)

    if len(args) == 2:
        topclassname = args[1]
    else:
        topclassname = ""

    process_json(
        args[0], 
        output,
        topclassname,
        options.public_fields if options.public_fields else False,
        options.getset if options.getset else True
    )

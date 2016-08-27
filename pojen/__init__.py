import json_parser
import file_handler
import engine
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


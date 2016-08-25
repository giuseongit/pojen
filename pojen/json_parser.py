import json

# This function only exists for the possipility to change
# the parser, if necessary, and leave the rest of the 
# application untouched
def parse(json_obj):
    return json.loads(json_obj)
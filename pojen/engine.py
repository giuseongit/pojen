import builders

java_types = {
    bool: "boolean",
    float: "float",
    int: "int",
    str: "String"
}

java_types_array = {
    bool: "Boolean",
    float: "Float",
    int: "Integer",
    str: "String"
}

def generate_classes(structures, public_fields=False, getset=True):
    classes = []

    for classname, struct in structures:
        t_class = builders.generate_class(classname, struct, public_fields, getset)
        classes.append((classname, t_class))

    return classes

def prepare_structure(classname, obj):
    classes = []
    element = {}
    classes.append((classname,element))

    for key, value in obj.items():
        if type(value) == dict:
            dt = prepare_structure(key, value)
            classes += dt
            element[key] = key.title()
        elif type(value) == list:
            if len(value) > 0 and type(value[0]) == dict:
                ls = prepare_structure(key, value[0])
                classes += ls
                element[key] = "ArrayList<{}>".format(key.title())
            elif len(value) > 0:
                element[key] = "ArrayList<{}>".format(java_types_array[infer_type(value[0])])
            else:
                element[key] = "ArrayList<String>"
        else:
            element[key] = java_types[infer_type(value)]

    return classes


def infer_type(obj):
    if obj == "true" or obj == "false":
        return bool
    elif can_parse_float(obj):
        return float
    elif can_parse_int(obj):
        return int
    else:
        return str

def can_parse_int(num):
    if type(num) == int:
        return True
    elif type(num) == str:
        try:
            int(num)
        except ValueError:
            return False
        return True

def can_parse_float(num):
    if type(num) == float:
        return True
    elif type(num) == str:
        if len(num.split(".")) == 1:
            return False
        try:
            float(num)
        except ValueError:
            return False
        return True
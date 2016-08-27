def method(method_name, acc_modifier, return_type, params, body):
    param_string = ""
    if params:
        for name, var_type in params.items():
            param_string += "{} {},".format(var_type, name)
        param_string = param_string[:-1]

    return """    {} {} {}({}){{{}}}""".format(acc_modifier, return_type, method_name, param_string, body)

def generate_import(package):
    return "import {};".format(package)

def getter(varname, vartype):
    body = "\n        return this.{};\n    ".format(varname)
    return method("get"+upperfirst(varname), "public", vartype, None, body)

def setter(varname, vartype):
    body = "\n        this.{} = {};\n    ".format(varname, varname)
    return method("set"+upperfirst(varname), "public", "void", {varname: vartype}, body)

def field(varname, vartype, acc_modifier):
    return "{} {} {};".format(acc_modifier, vartype, varname)

def generate_class(classname, fields, public_fields=False, getset=True, imports=[]):
    imports_string = ""
    for elem in imports:
        imports_string += "{}\n".format(generate_import(elem))
    if len(imports) > 0:
        imports_string += "\n"

    _fields = ""
    acc_modifier = "public" if public_fields else "private"
    for varname, vartype in fields.items():
        _fields += "    {}\n".format(field(varname, vartype, acc_modifier))

    _methods = ""
    if getset:
        for varname, vartype in fields.items():
            _methods += "{}\n\n{}\n\n".format(getter(varname, vartype), setter(varname, vartype))

    return "{}public class {}{{\n{}\n\n{}}}".format(imports_string, upperfirst(classname), _fields, _methods)

def upperfirst(x):
    return x[0].upper() + x[1:] if len(x) > 0 else ""
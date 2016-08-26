def method(method_name, acc_modifier, return_type, params, body):
    param_string = ""
    if params:
        for name, var_type in params.items():
            param_string += "{} {},".format(var_type, name)
        param_string = param_string[:-1]    

    return """    {} {} {}({}){{{}}}""".format(acc_modifier, return_type, method_name, param_string, body)

def getter(varname, vartype):
    body = "\n        return this.{};\n    ".format(varname)
    return method("get"+(varname.title()), "public", vartype, None, body)

def setter(varname, vartype):
    body = "\n        this.{} = {};\n    ".format(varname, varname)
    return method("set"+(varname.title()), "public", "void", {varname: vartype}, body)

def field(varname, vartype, acc_modifier):
    return "{} {} {};".format(acc_modifier, vartype, varname)

def generate_class(classname, fields, public_fields=False, getset=True):
    _fields = ""
    acc_modifier = "public" if public_fields else "private"
    for varname, vartype in fields.items():
        _fields += "    {}\n".format(field(varname, vartype, acc_modifier))

    _methods = ""
    if getset:
        for varname, vartype in fields.items():
            _methods += "{}\n\n{}\n\n".format(getter(varname, vartype), setter(varname, vartype))

    return "public class {}{{\n{}\n\n{}}}".format(classname, _fields, _methods)

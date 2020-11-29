# this part of the Jack Compiler takes identifers from source code and organises
# them with indexs

class_table = {} # name : [{type}, {kind}, {index}]

subroutine_table = {} # name : [{type}, {kind}, {index}]


def constructor():# creates a new symbol table
    items = class_table.items()
    class_table.clear
    for key, value in items:
        if value[1] == "static":
            class_table[key] = value
    subroutine_table.clear()


def startSubroutine():# start a new subroutine scope; clear locals/ args
    subroutine_table.clear()


def define(name, type, kind):# defines a new identifier of the name {name}, the type {type} and kind {kind}

    # class scope variables
    if kind in ["field", "static"]:
        # find out how many items of the same kind are in the table
        index = len([value for value in class_table.values() if value[1] == kind])
        class_table[name] = [type, kind, index]

    # subroutine scope variable
    if kind in ["argument", "local"]:
        # find out how many items of the same kind are in the table
        index = len([value for value in subroutine_table.values() if value[1] == kind])
        subroutine_table[name] = [type, kind, index]


def VarCount(kind):# returns (int) number of variables of given kind in current scope
    if kind in ["field", "static"]:
        return len([value for value in class_table if value[1] == kind])

    elif kind in ["argument", "local"]:
        return len([value for value in subroutine_table if value[1] == kind])


def KindOf(name):# returns (string) the kind of the identifier {name} in current scope
    if name in subroutine_table.keys():
        return subroutine_table[name][1]
    else:
        return class_table[name][1]


def TypeOf(name):# returns (string) the type of the identifier {name} in current scope
    if name in subroutine_table.keys():
        return subroutine_table[name][0]
    else:
        return class_table[name][0]


def IndexOf(name):# returns (int) the index of the identifier {name}
    if name in subroutine_table.keys():
        return subroutine_table[name][2]
    else:
        return class_table[name][2]

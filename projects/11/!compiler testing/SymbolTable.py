# this part of the Jack Compiler takes identifers from source code and organises
# them with indexs

class_table = {}                                                                # name : [{type}, {kind}, {index}]

subroutine_table = {}                                                           # name : [{type}, {kind}, {index}]

sym_tables = {"STATIC"      : class_table,                                      # used to add to find the correct symbol table for each segment
              "FIELD"       : class_table,
              "ARG"         : subroutine_table,
              "VAR"         : subroutine_table}

def constructor():                                                              # creates a new symbol table
    items = class_table.items()
    class_table.clear()                                                         # keep static identifers across classes
    for key, value in items:
        if value[1] == "STATIC":
            class_table[key] = value
    subroutine_table.clear()


def startSubroutine():                                                          # start a new subroutine scope; clear locals/ args
    subroutine_table.clear()


def define(name, type, kind):                                                   # defines a new identifier of the name {name}, the type {type} and kind {kind}
    correct_table = sym_tables[kind]                                            #   find correct table                                                           #   -1 means index should be automatically assigned
    index = len([1 for value in correct_table.values() if value[1] == kind])    #   find out how many items of the same kind are in the table
    correct_table[name] = [type, kind, index]                                   #   add to correct table


def VarCount(kind):                                                             # returns (int) number of variables of given kind in current scope
    correct_table = sym_tables[kind]
    return len([1 for value in correct_table.values() if value[1] == kind])


def KindOf(name):                                                               # returns (string) the kind of the identifier {name} in current scope
    if name in subroutine_table.keys():
        return subroutine_table[name][1]
    elif name in class_table.keys():
        return class_table[name][1]
    else:
        return None


def TypeOf(name):                                                               # returns (string) the type of the identifier {name} in current scope
    if name in subroutine_table.keys():
        return subroutine_table[name][0]
    elif name in class_table.keys():
        return class_table[name][0]
    else:
        return None


def IndexOf(name):                                                              # returns (int) the index of the identifier {name}
    if name in subroutine_table.keys():
        return subroutine_table[name][2]
    elif name in class_table.keys():
        return class_table[name][2]
    else:
        return None

# the file that parses a .vm file to split the vm instructions into their parts

# conversion table between commands and the API strings
command_types = {   "push"      :   "C_PUSH",
                    "pop"       :   "C_POP",
                    "label"     :   "C_LABEL",
                    "goto"      :   "C_GOTO",
                    "if-goto"   :   "C_IF",
                    "function"  :   "C_FUNCTION",
                    "return"    :   "C_RETURN",
                    "call"      :   "C_CALL"}


# variables used during execution
commands_list = []
current_command = None
command_type = None
arg_1 = None
arg_2 = None

def initialise(vm_file): # initialise with file stream
    lines_list = vm_file.read_text().split("\n")

    for line in lines_list:
        if "//" in line: # remove comments
            line = line[:line.find("//")]

        line = line.strip()
        if len(line) != 0: # don't add empty lines
            commands_list.append(line)


def hasMoreCommands(): # returns (bool) if there are more commands
    return len(commands_list) != 0


def advance(): # move on to next command
    global current_command, command_type, arg_1, arg_2

    current_command = commands_list.pop(0) # select next command
    words = current_command.strip().split(' ') # process current command

    if words[0] in command_types : # other commands
        command_type = command_types[words[0]]
        #print(command_type)

        if command_type != "C_RETURN": # only put an arg 1 if it is not a return
            arg_1 = words[1]
        else:
            arg_1 = None

        if command_type in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]: # only put an arg 2 if it is an instruction with one
            arg_2 = words[2]
        else:
            arg_2 = None

    else: # arithmetic commands
        command_type = "C_ARITHMETIC"
        arg_1 = words[0]
        arg_2 = None


def commandType(): # returns (string) the command type
    return command_type

def arg1(): # returns (string) first argument: arithmetic command or memory segment
    return arg_1


def arg2(): # returns (int) second argument: segment based memory address
    return arg_2

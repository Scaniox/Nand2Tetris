
# functions
def initialise(lines_list):
    global current_command_index, current_command, commands_list

    current_command_index = 0
    current_command = ""

    # read lines from file:
    commands_list = []

    # remove comments and blank lines
    for command in lines_list :

        # remove comments
        if  "//" in command :
            command = command[:command.find("//")]

        if not(len(command.strip()) == 0) : # only add non blank lines to commands_list
            commands_list.append(command.strip())

    # set up first command:
    current_command = commands_list[0].strip()


def hasMoreCommands():# return (bool) if there is another command to assemble
    global current_command_index, current_command, commands_list

    return len(commands_list) > current_command_index+1


def advance(): # move onto the next command
    global current_command_index, current_command, commands_list

    current_command_index += 1
    current_command = commands_list[current_command_index].strip()

def commandType(): # return (string) what kind of command the current command is
    global current_command

    if current_command[0] == '@' :
        return "A_COMMAND"

    elif current_command[0] == '(' :
        return "L_COMMAND"

    else:
        return "C_COMMAND"


def symbol(): # return (string) the number/symbol of an A instruction
    global current_command
    return current_command[1:]

def dest(): # return (string) destination of a C intruction
    global current_command
    if '=' in current_command : # there is a destination
        return current_command[:current_command.find('=')].strip()

    else:
        return "null"


def comp(): # return (string) computation mnemonic
    global current_command

    computation = current_command

    if '=' in computation : # remove dest
        computation = computation[computation.find('=')+1:].strip()

    if ';' in computation : # remove jump
        computation = computation[:computation.find(';')].strip()

    return computation


def jump(): # return (string) jump mnemonic
    global current_command

    if ';' in current_command :
        return current_command[current_command.find(';')+1:].strip()

    else :
        return "null"

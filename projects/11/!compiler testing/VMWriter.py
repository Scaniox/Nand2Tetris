# this part of the Jack Compiler generates the code for the VM
cursor = 0


def constructor(file):# initialises vm writer with a file
    global output_file, output_text
    output_text = ""
    output_file = file


def WritePush(segment, index):# write vm code to push a value from a memory segment onto the stack
    global output_text
    output_text += f"push {segment.lower()} {index}\n"


def WritePop(segment, index):# write vm code to pop a value from the stack
    global output_text
    output_text += f"pop {segment.lower()} {index}\n"


def WriteArithmetic(command):# write vm code for arithmetic
    global output_text
    output_text += f"{command.lower()}\n"


def WriteLabel(label):# write vm code to generate a label
    global output_text
    output_text += f"label {label}\n"


def WriteGoto(label):# write vm code to branch
    global output_text
    output_text += f"goto {label}\n"


def WriteIf(label):# write vm code to conditional branch
    global output_text
    output_text += f"if-goto {label}\n"


def WriteCall(name, nArgs):# write vm code to call a function
    global output_text
    output_text += f"call {name} {nArgs}\n"


def WriteFunction(name, nLocals):# write vm code to define a function
    global output_text
    output_text += f"function {name} {nLocals}\n"


def WriteReturn():# write vm code to return
    global output_text
    output_text += f"return\n"


def close():# close output file
    global output_text
    output_file.write_text(output_text)

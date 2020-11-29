# this part of the Jack Compiler generates the code for the VM


def constructor(file):# initialises vm writer with a file
    global output_file
    output_file = file


def WritePush(segment, index):# write vm code to push a value from a memory segment onto the stack
    output_file.write(f"push {segment.lower()} {index}\n")


def WritePop(segment, index):# write vm code to pop a value from the stack
    output_file.write(f"pop {segment.lower()} {index}\n")


def WriteArithmetic(command):# write vm code for arithmetic
    output_file.write(f"{command.lower()}\n")


def WriteLabel(label):# write vm code to generate a label
    output_file.write(f"label {label}\n")


def WriteGoto(label):# write vm code to branch
    output_file.write(f"goto {label}\n")


def WriteIf(label):# write vm code to conditional branch
    output_file.write(f"if-goto {label}\n")


def WriteCall(name, nArgs):# write vm code to call a function
    output_file.write(f"call {name} {nArgs}\n")


def WriteFunction(name, nLocals):# write vm code to define a function
    output_file.write(f"function {name} {nArgs}\n")


def WriteReturn():# write vm code to return
    output_file.write(f"return\n")


def close():# close output file
    pass
